import os

import streamlit as st
from LLM.chain import *
from src.main import *
# from audio_recorder_streamlit import audio_recorder
from streamlit_mic_recorder import speech_to_text
from deep_translator import GoogleTranslator
from gtts import gTTS
import base64



def voice_input(lang):
    # recorded_audio=audio_recorder(pause_threshold=2.0, sample_rate=44_000)
    text = speech_to_text(
    language=lang,
    start_prompt="🔴",
    stop_prompt="🟥",
    just_once=False,
    use_container_width=False,
    callback=None,
    args=(),
    kwargs={},
    key=None
    )
    print(text)
    return text

def usertrans(user_input,lang):
    translated = GoogleTranslator(source=lang,target='en').translate(user_input)
    return translated

def bottrans(response,lang):
    translated= GoogleTranslator(source='en',target=lang).translate(response)
    return translated

def texttoaudio(text,lang):
    tts = gTTS(text,lang=lang)
    tts.save('response.mp3')
    
def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio controls autoplay="true">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(
            md,
            unsafe_allow_html=True,
        )
        st.write("# Auto-playing Audio!")