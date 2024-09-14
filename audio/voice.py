import os

import streamlit as st
from LLM.chain import *
from src.main import *
# from audio_recorder_streamlit import audio_recorder
from streamlit_mic_recorder import speech_to_text


def voice_input():
    # recorded_audio=audio_recorder(pause_threshold=2.0, sample_rate=44_000)
    text = speech_to_text(
    language='hi',
    start_prompt="Start recording",
    stop_prompt="Stop recording",
    just_once=False,
    use_container_width=False,
    callback=None,
    args=(),
    kwargs={},
    key=None
    )
    return text