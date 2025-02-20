import re
from pathlib import Path

import numpy as np
import soundfile as sf
import streamlit as st

from document_to_podcast.inference.text_to_speech import text_to_speech
from document_to_podcast.preprocessing import DATA_LOADERS, DATA_CLEANERS
from document_to_podcast.inference.model_loaders import (
    load_llama_cpp_model,
    load_tts_model,
)
from document_to_podcast.config import DEFAULT_PROMPT, DEFAULT_SPEAKERS, Speaker
from document_to_podcast.inference.text_to_text import text_to_text_stream


@st.cache_resource
def load_text_to_text_model():
    return load_llama_cpp_model(
        model_id="allenai/OLMoE-1B-7B-0924-Instruct-GGUF/olmoe-1b-7b-0924-instruct-q8_0.gguf"
    )


@st.cache_resource
def load_text_to_speech_model():
    return load_tts_model("OuteAI/OuteTTS-0.2-500M-GGUF/OuteTTS-0.2-500M-FP16.gguf")


script = "script"
audio = "audio"
gen_button = "generate podcast button"
if script not in st.session_state:
    st.session_state[script] = ""
if audio not in st.session_state:
    st.session_state.audio = []
if gen_button not in st.session_state:
    st.session_state[gen_button] = False


def gen_button_clicked():
    st.session_state[gen_button] = True


st.title("Document To Podcast")

st.header("Uploading Data")

uploaded_file = st.file_uploader(
    "Choose a file", type=["pdf", "html", "txt", "docx", "md"]
)


if uploaded_file is not None:
    st.divider()
    st.header("Loading and Cleaning Data")
    st.markdown(
        "[Docs for this Step](https://mozilla-ai.github.io/document-to-podcast/step-by-step-guide/#step-1-document-pre-processing)"
    )
    st.divider()

    extension = Path(uploaded_file.name).suffix

    col1, col2 = st.columns(2)

    raw_text = DATA_LOADERS[extension](uploaded_file)
    with col1:
        st.subheader("Raw Text")
        st.text_area(
            f"Number of characters before cleaning: {len(raw_text)}",
            f"{raw_text[:500]} . . .",
        )

    clean_text = DATA_CLEANERS[extension](raw_text)
    with col2:
        st.subheader("Cleaned Text")
        st.text_area(
            f"Number of characters after cleaning: {len(clean_text)}",
            f"{clean_text[:500]} . . .",
        )

    st.divider()
    st.header("Downloading and Loading models")
    st.markdown(
        "[Docs for this Step](https://mozilla-ai.github.io/document-to-podcast/step-by-step-guide/#step-2-podcast-script-generation)"
    )
    st.divider()

    st.markdown(
        "For this demo, we are using the following models: \n"
        "- [OLMoE-1B-7B-0924-Instruct](https://huggingface.co/allenai/OLMoE-1B-7B-0924-Instruct-GGUF)\n"
        "- [OuteAI/OuteTTS-0.2-500M-GGUF/OuteTTS-0.2-500M-FP16.gguf](https://huggingface.co/OuteAI/OuteTTS-0.2-500M-GGUF)"
    )
    st.markdown(
        "You can check the [Customization Guide](https://mozilla-ai.github.io/document-to-podcast/customization/)"
        " for more information on how to use different models."
    )

    text_model = load_text_to_text_model()
    speech_model = load_text_to_speech_model()

    # ~4 characters per token is considered a reasonable default.
    max_characters = text_model.n_ctx() * 4
    if len(clean_text) > max_characters:
        st.warning(
            f"Input text is too big ({len(clean_text)})."
            f" Using only a subset of it ({max_characters})."
        )
        clean_text = clean_text[:max_characters]

    st.divider()
    st.header("Podcast generation")
    st.markdown(
        "[Docs for this Step](https://mozilla-ai.github.io/document-to-podcast/step-by-step-guide/#step-3-audio-podcast-generation)"
    )
    st.divider()

    st.subheader("Speaker configuration")
    for s in DEFAULT_SPEAKERS:
        s.pop("id", None)
    speakers = st.data_editor(DEFAULT_SPEAKERS, num_rows="dynamic")

    if st.button("Generate Podcast", on_click=gen_button_clicked):
        for n, speaker in enumerate(speakers):
            speaker["id"] = n + 1
        speakers_str = "\n".join(
            str(Speaker.model_validate(speaker))
            for speaker in speakers
            if all(
                speaker.get(x, None) for x in ["name", "description", "voice_profile"]
            )
        )
        system_prompt = DEFAULT_PROMPT.replace("{SPEAKERS}", speakers_str)
        with st.spinner("Generating Podcast..."):
            text = ""
            for chunk in text_to_text_stream(
                clean_text, text_model, system_prompt=system_prompt.strip()
            ):
                text += chunk
                if text.endswith("\n") and "Speaker" in text:
                    st.session_state.script += text
                    st.write(text)

                    speaker_id = re.search(r"Speaker (\d+)", text).group(1)
                    voice_profile = next(
                        speaker["voice_profile"]
                        for speaker in speakers
                        if speaker["id"] == int(speaker_id)
                    )
                    with st.spinner("Generating Audio..."):
                        speech = text_to_speech(
                            text.split(f'"Speaker {speaker_id}":')[-1],
                            speech_model,
                            voice_profile,
                        )
                    st.audio(speech, sample_rate=speech_model.sample_rate)

                    st.session_state.audio.append(speech)
                    text = ""

    if st.session_state[gen_button]:
        if st.button("Save Podcast to audio file"):
            st.session_state.audio = np.concatenate(st.session_state.audio)
            sf.write(
                "podcast.wav",
                st.session_state.audio,
                samplerate=speech_model.sample_rate,
            )
            st.markdown("Podcast saved to disk!")

        if st.button("Save Podcast script to text file"):
            with open("script.txt", "w") as f:
                st.session_state.script += "}"
                f.write(st.session_state.script)

            st.markdown("Script saved to disk!")
