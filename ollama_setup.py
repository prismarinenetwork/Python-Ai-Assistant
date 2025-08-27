import os
import time
usr_prof=os.environ['USERPROFILE']
os.chdir(usr_prof+'\Downloads')
print('Installing ollama ai...')
os.system('curl -sSL https://ollama.com/download/OllamaSetup.exe -o OllamaSetup.exe')
print('Done !')
print('Attempting to execute the file')
try:
    os.system('OllamaSetup.exe')
except:
    print('Could not execute file try running the ollama setup manually')
    print('(Check your downloads folder for the ollamasetup file)')
print('')
print('Done with everything ! you may now close this terminal.')
time.sleep(999999)
