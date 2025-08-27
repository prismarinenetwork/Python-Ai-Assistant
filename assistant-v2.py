#Im Just going to let you know before you read this file that all of the code below is joy coded so it could be optimized but I made this for fun so its fine I guess.
























import os
def install_pip():
    os.system('curl -sSL https://bootstrap.pypa.io/get-pip.py -o get-pip.py')
    os.system('get-pip.py')
    os.remove('get-pip.py')    
install_pip()

try:
    import ollama
except:
    os.system('pip install ollama')
try:
    from gtts import gTTS
except:
    os.system('pip install gtts')
try:
    import pygame
except:
    os.system('pip install pygame')
try:
    import speech_recognition as sr
except:
    os.system('pip install SpeechRecognition')
try:
    import keyboard
except:
    os.system('pip install keyboard')
try:
    #It says it's not used but whenever I dont use this it errors so we keeping it
    import pyaudio
except:
    os.system('pip install pyaudio')
try:
    import whisper
except:
    os.system('pip install -U openai-whisper')
try:
    import pyttsx3
except:
    os.system('pip install pyttsx3')
try:
    import soundfile
except:
    os.system('pip install soundfile')
import ollama
from gtts import gTTS
import pygame 
import speech_recognition as sr
import keyboard
import time
import threading
import random
import pyttsx3




os.system('cls')
def record_mic():
    global filename
    recognizer = sr.Recognizer()
    mic = sr.Microphone(device_index=1)
    audio_chunks = []

    with mic as source:
        while keyboard.is_pressed('`'):
            audio = recognizer.listen(source, phrase_time_limit=1)
            audio_chunks.append(audio)

    if not audio_chunks:
        return None
    

    combined_audio = sr.AudioData(
        b''.join(chunk.get_raw_data() for chunk in audio_chunks),
        sample_rate=audio_chunks[0].sample_rate,
        sample_width=audio_chunks[0].sample_width
    )
    
    
    whisper_voice_rec=recognizer.recognize_whisper(combined_audio, language="english", model="base")
    print('You said:'+whisper_voice_rec)
    print('')
    ai_output = ollama.generate(model='qwen2.5vl:3b', prompt=whisper_voice_rec)
    ai_output = ai_output['response']
    print('Ai response:'+str(ai_output))
    print('')
    engine = pyttsx3.init()
    engine.setProperty('rate', 190) 
    engine.say(ai_output)
    engine.runAndWait()
print('Listening for input...')
while True:
    if keyboard.is_pressed('`'):
        mp3File=record_mic()
        while keyboard.is_pressed('`'):
            pass
#['tiny.en', 'tiny', 'base.en', 'base', 'small.en', 'small', 'medium.en', 'medium', 'large-v1', 'large-v2', 'large-v3', 'large', 'large-v3-turbo', 'turbo']
