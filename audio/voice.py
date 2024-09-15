import os

import streamlit as st
from LLM.chain import *
from src.main import *
# from audio_recorder_streamlit import audio_recorder
from streamlit_mic_recorder import speech_to_text
from deep_translator import GoogleTranslator
from streamlit_TTS import auto_play, text_to_speech, text_to_audio




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
    translated= GoogleTranslator(source=lang,target='hi').translate(response)
    return translated

def texttoaudio(text,lang):
    audio=text_to_audio(text,language=lang)
    auto_play(audio)