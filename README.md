[![](https://dcbadge.limes.pink/api/server/YuMNeuKStr?style=flat)](https://discord.gg/YuMNeuKStr)
[![Docs](https://github.com/mozilla-ai/document-to-podcast/actions/workflows/docs.yaml/badge.svg)](https://github.com/mozilla-ai/document-to-podcast/actions/workflows/docs.yaml/)
[![Tests](https://github.com/mozilla-ai/document-to-podcast/actions/workflows/tests.yaml/badge.svg)](https://github.com/mozilla-ai/document-to-podcast/actions/workflows/tests.yaml/)
[![Ruff](https://github.com/mozilla-ai/document-to-podcast/actions/workflows/lint.yaml/badge.svg?label=Ruff)](https://github.com/mozilla-ai/document-to-podcast/actions/workflows/lint.yaml/)

<p align="center"><img src="./images/Blueprints-logo.png" width="35%" alt="Project logo"/></p>

# Document-to-podcast: Experimenting with different languages!

For more up-to-date information, please visit the [original repo](https://github.com/mozilla-ai/document-to-podcast).

This repo showcases how to use the `document-to-podcast` tool with languages other than English. 


## Supported languages

### Text-to-Text (script generation)

Most of the SOTA LLMs right now can perform quite well in different languages without any tweaking. Our default model [OLMoE](https://huggingface.co/collections/allenai/olmoe-66cf678c047657a30c8cd3da), seems to be able to handle multiple languages relatively well, but there is no official documentation on which languages it supports. If you feel you are not getting a script that is convincing enough in the language you want, feel free to change the `text-to-text` model by following the instructions in the [docs](https://mozilla-ai.github.io/document-to-podcast/). 

### Text-to-Speech (audio generation)

Since these models keep evolving, for an updated list of all languages and speakers please visit their respective websites.

-  [x] `parler-tts/parler-tts-mini-multilingual-v1.1` [HF](https://huggingface.co/parler-tts/parler-tts-mini-multilingual-v1.1) - [Speaker list](https://huggingface.co/parler-tts/parler-tts-mini-multilingual-v1.1#%F0%9F%8E%AF-using-a-specific-speaker)
    - [x] Portuguese ( `Sophia` & `Nicholas`)
    - [x] Dutch ( `Mark` & `Jessica`)
    - [x] French ( `Daniel` & `Christine`)
    - [x] German ( `Nicole` & `Michelle`)
    - [x] Italian ( `Julia` & `Richard`)
    - [x] Polish ( `Alex` & `Natalie`)
    - [x] Spanish ( `Steven` & `Olivia`)
-  [x] `ai4bharat/indic-parler-tts`  [HF](https://huggingface.co/ai4bharat/indic-parler-tts) - [Speaker list](https://huggingface.co/ai4bharat/indic-parler-tts#%F0%9F%8E%AF-using-a-specific-speaker)
    - [x] Assamese ( `Amit` & `Sita`)
    - [x] Bengali ( `Arjun` & `Aditi`)
    - [x] Bodo ( `Bikram` & `Maya`)
    - [x] Chhattisgarhi ( `Bhanu` & `Champa`)
    - [x] Dogri ( `Karan` & `Karan`)
    - [x] Gujarati ( `Yash` & `Neha`)
    - [x] Hindi ( `Rohit` & `Divya`)
    - [x] Kannada ( `Suresh` & `Anu`)
    - [x] Malayalam ( `Anjali` & `Harish`),
    - [x] Manipuri ( `Laishram` & `Ranjit`),
    - [x] Marathi ( `Sanjay` & `Sunita`),
    - [x] Nepali ( `Amrita` & `Amrita`)
    - [x] Odia ( `Manas` & `Debjani`),
    - [x] Punjabi ( `Divjot` & `Gurpreet`),
    - [x] Sanskrit ( `Aryan` & `Aryan`)
    - [x] Tamil ( `Jaya` & `Jaya`)
    - [x] Telugu ( `Prakash` & `Lalitha`)
- [x] `suno/bark` [GitHub](https://github.com/suno-ai/bark) - [Speaker hub](https://suno-ai.notion.site/8b8e8749ed514b0cbf3f699013548683?v=bc67cff786b04b50b3ceb756fd05f68c)
    - [x] German ( `v2/de_speaker_0` & `v2/de_speaker_1`)
    - [x] Spanish ( `v2/es_speaker_0` & `v2/es_speaker_8`)
    - [x] French ( `v2/fr_speaker_0` & `v2/fr_speaker_1`)
    - [x] Hindi ( `v2/hi_speaker_0` & `v2/hi_speaker_1`)
    - [x] Italian ( `v2/it_speaker_0` & `v2/it_speaker_1`)
    - [x] Japanese ( `v2/ja_speaker_0` & `v2/ja_speaker_1`)
    - [x] Korean ( `v2/ko_speaker_0` & `v2/ko_speaker_1`)
    - [x] Polish ( `v2/pl_speaker_0` & `v2/pl_speaker_1`)
    - [x] Portuguese ( `v2/pt_speaker_0` & `v2/pt_speaker_1`)
    - [x] Russian ( `v2/ru_speaker_0` & `v2/ru_speaker_1`)
    - [x] Turkish ( `v2/tr_speaker_0` & `v2/tr_speaker_1`)
    - [x] Chinese ( `v2/zh_speaker_0` & `v2/zh_speaker_1`)
- [x] `OuteTTS-0.2-500M` [GitHub](https://github.com/edwko/OuteTTS) - [Speaker list](https://github.com/edwko/OuteTTS/blob/main/outetts/version/v1/interface.py#L31)
    - [x] Japanese (`female_1` & `male_1`)
    - [x] Korean (`female_1` & `male_1`)
    - [x] Chinese (`female_1` & `male_1`)
    - [x] Korean (`female_1` & `male_1`)



### Built with
- Python 3.10+ (use Python 3.12 for Apple M1/2/3 chips)
- [Llama-cpp](https://github.com/abetlen/llama-cpp-python) (text-to-text, i.e script generation)
- [OuteAI](https://github.com/edwko/OuteTTS) / [Bark](https://github.com/suno-ai/bark) / [Parler_tts](https://github.com/huggingface/parler-tts) (text-to-speech, i.e audio generation)
- [Streamlit](https://streamlit.io/) (UI demo)



## Usage

1. **Install the package**
   ```bash
   pip install document-to-podcast
   ```

2. **Set your configuration**:
   1. **Pick a model from the list above, based on the language you want to try**.
   
       For example: `parler-tts/parler-tts-mini-multilingual-v1.1`
   
   2. **Edit the `example_data/config.yaml` with your configuration**

       Specifically, you should update the following parameters:

       `input_file`: Use a file that has text in a language of your choice

       `text_to_speech_model`: Use one of the model ids, defined above, based on the language you are testing

       `text_to_text_prompt`: Re-write it / Translate it in the testing language

       `speaker/description`: Re-write it / Translate it in the testing language

       `voice_profile`: Use one of the pre-defined profiles based on the testing language, from the list above
   
        `outetts_language` (Only for models from the [OuteAI](https://github.com/edwko/OuteTTS) family): You need to add this argument at the bottom of your config and add a supported language like `en, zh, ja, ko`.

3. **Generate the podcast**
   Inside the terminal, run the CLI:
   ```bash
   document-to-podcast --from_config example_data/config.yaml
   ```
   _Note: If you don't want to wait for the whole podcast to be generated you can stop it mid-way, by pressing Ctrl+C in the terminal that you are running the process. It will stop and save the script and audio up until that point!_

4. **Verify everything worked as expected by checking `podcast.txt` and `podcast.wav`**

***NOTE***: The first time you run the demo app it might take a while to generate the script or the audio because it will download the models to the machine which are a few GBs in size.


## Pre-requisites

- **System requirements**:
  - OS: Windows, macOS, or Linux
  - Python 3.10>, <3.12
  - Minimum RAM: 10 GB
  - Disk space: 32 GB minimum

- **Dependencies**:
  - Dependencies listed in `pyproject.toml`


## License

This project is licensed under the Apache 2.0 License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! To get started, you can check out the [CONTRIBUTING.md](CONTRIBUTING.md) file.
