#Im Just going to let you know before you read this file that all of the code below is joy coded so don't expect anything crazy
























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
import ollama
from gtts import gTTS
import pygame 
import speech_recognition as sr
import keyboard
import time
import threading
import random

def random_filename():
        #Before you say anything I know there is a faster way but this was coded at 3:00 AM
        global filename
        filename=''
        random_1=random.choice(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
        random_2=random.choice(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
        random_3=random.choice(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
        random_4=random.choice(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
        random_5=random.choice(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
        random_6=random.choice(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
        random_7=random.choice(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
        random_8=random.choice(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
        random_9=random.choice(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
        random_10=random.choice(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
        random_11=random.choice(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
        random_12=random.choice(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
        random_13=random.choice(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
        random_14=random.choice(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
        random_num_1=random.choice(['1','2','3','4','5','6','7','8','9','0'])
        random_num_2=random.choice(['1','2','3','4','5','6','7','8','9','0'])
        random_num_3=random.choice(['1','2','3','4','5','6','7','8','9','0'])
        random_num_4=random.choice(['1','2','3','4','5','6','7','8','9','0'])
        random_num_5=random.choice(['1','2','3','4','5','6','7','8','9','0'])
        random_num_6=random.choice(['1','2','3','4','5','6','7','8','9','0'])
        random_num_7=random.choice(['1','2','3','4','5','6','7','8','9','0'])
        random_num_8=random.choice(['1','2','3','4','5','6','7','8','9','0'])
        random_num_9=random.choice(['1','2','3','4','5','6','7','8','9','0'])
        random_num_0=random.choice(['1','2','3','4','5','6','7','8','9','0'])
        filename=random_1+random_2+random_3+random_4+random_5+random_6+random_7+random_8+random_9+random_10+random_11+random_12+random_13+random_14+random_num_1+random_num_2+random_num_3+random_num_4+random_num_5+random_num_6+random_num_7+random_num_8+random_num_9+random_num_0
        return filename
usr_prof=os.environ['USERPROFILE']
os.chdir(usr_prof+'/Downloads')

def play_file(mp3File):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
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
    
    
    whisper_voice_rec=recognizer.recognize_whisper(combined_audio, language="english", model="medium")
    print('You said:'+whisper_voice_rec)
    print('')
    ai_output = ollama.generate(model='openchat:7b', prompt=whisper_voice_rec)
    ai_output = ai_output['response']
    print('Ai response:'+str(ai_output))
    print('')
    tts = gTTS(ai_output,slow=False)
    filename=str(random_filename())+'.mp3'
    tts.save(filename)
    return ai_output
def music_helper(mp3File):
    while pygame.mixer.music.get_busy():
        time.sleep(0.50)
    pygame.mixer.music.stop()
    


while True:
    if keyboard.is_pressed('`'):
        mp3File=record_mic()
        if mp3File:
            playing_file_thread=threading.Thread(target=play_file, args=(mp3File,)).start()
            music_helper_thread=threading.Thread(target=music_helper, args=(mp3File,)).start()
            
        while keyboard.is_pressed('`'):
            pass
#['tiny.en', 'tiny', 'base.en', 'base', 'small.en', 'small', 'medium.en', 'medium', 'large-v1', 'large-v2', 'large-v3', 'large', 'large-v3-turbo', 'turbo']
