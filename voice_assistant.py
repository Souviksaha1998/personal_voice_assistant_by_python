from subprocess import TimeoutExpired
import pyautogui
import pyttsx3
import speech_recognition as sr
import wikipedia
import time
import datetime
import pyaudio
import webbrowser
import os
import random
# import sys
import requests
import pywhatkit as kit
import random
import pyjokes
import os
import winshell
import sys
# import cv2
print("Initializing Marshmellow for Souvik.....")
NAME = "souvik"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    mint = int(datetime.datetime.now().minute)
    second= int(datetime.datetime.now().second)
#speak(hour)
    print(hour)
    if hour >=0 and hour < 12:
        speak ("good morning .." )
    elif hour >=12 and hour <18:
        speak("good afternoon  .." )
    else:
        speak("good evening ")
def Marshmellow():
    if Marshmellow==takeCommand().lower():
        speak('yes boss')
    else:
        speak('sorry boss')
def takeCommand():

    r = sr.Recognizer()

    with sr.Microphone(device_index = 0) as source:
        r.adjust_for_ambient_noise(source )
        print("listening.....")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f" Boss Said : {query}\n")

    except:
        # speak(' i could not get it boss ... say that again')
        # print("say that again...")
        return 'None'
        
    return query

def task():
    wishMe()
    speak("hi boss ")
    speak("how can i help you??....")
    while (1):
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            print("According to wikipedia....")
            speak("According to wikipedia...")
            print(results)
            speak(results)
        elif 'open youtube' in query or 'youtube' in query:
            speak('what should i search boss??')
            print('what should i search boss??')
            m = takeCommand().lower()
            print(m)
            print('opening youtube...')
            speak(f'opening youtube and searching {m}')
            webbrowser.open('https://youtube.com/results?search_query=' + m)
            time.sleep(12)
            pyautogui.click(x = 410, y =319 , button='left')
            time.sleep(8)
            pyautogui.click(x = 764, y =484 , button='left')
        elif 'open google'  in query:
            print('what should i search  boss??')
            speak('what should i search  boss??')
            z = takeCommand().lower()
            print(z)
            print('searching boss , wait a second')
            speak('searching boss , wait a second')
            webbrowser.open('https://google.com/search?q=' + z)

        elif 'open browser' in query:
            print('what should i search  boss??')
            speak('what should i search  boss??')
            z = takeCommand().lower()
            print(z)
            print('opening browser...')
            speak(f'opening browser and searching {z}')
            webbrowser.open('https://google.com/search?q=' + z)
        elif 'play music' in query:
            music_dir = 'D:\\my faV. songs'
            songs= os.listdir(music_dir)
            d= random.choice(songs)
            os.startfile(os.path.join(music_dir, d))

        elif "play song on youtube" in query:
            speak('which song do you want to hear sir??')
            z = takeCommand().lower()
            speak(f'ok sir playing {z}')
            kit.playonyt(f'{z}')
            time.sleep(12)
            pyautogui.click(x = 410, y =319 , button='left')
            time.sleep(8)
            pyautogui.click(x = 764, y =484 , button='left')

        elif "time" in query:
            strcurrent_time =datetime.datetime.now().strftime("%H:%M")
            print(f'the time is {strcurrent_time}')
            speak(f'boss , the time is {strcurrent_time}')
        
        elif 'tell me a joke' in query:
            speak(pyjokes.get_jokes())
        elif 'lets play a game' in query or 'play game' in query:
            s =random.randint(1 ,10)
            print(s)
            i = 0
            while True:
                i +=1
                try:
                    user = int((input('enter your guess no : ')))
                    if s>user:
                        speak('umm !! add some number to it ')
                    elif s<user:
                        speak('umm !! reduce some number from it')
                    elif s==user:
                        speak(f'correct ,your number of guesses are {i}')
                        break
                except:
                    speak('enter number only')
                    speak('thank you for playing')
        elif 'exit' in query:
            speak('thank you for using me , sir')
            exit()
        elif 'stop listening' in query:
            speak("ok sir its break time now")
            break
            

        # elif 'shut down' or 'shut down computer' or 'ok shut down' in query:
        #     print("Shutting down the computer")
        #     speak("Shutting the computer")
        #     os.system("shutdown /s /t 30")

        # elif 'restart' or 'restart computer' or 'restart the computer ' or 'restart the computer now' in query:
        #     print("Shutting down the computer")
        #     speak("Shutting the computer")
        #     os.system("shutdown /r /t 30")
            

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak(f"boss asked to Locate{location}")
            webbrowser.open(f"https://www.google.co.in/maps/place/{location}")
        
        elif "will you be my gf" in query or "will you be my bf" in query:  
            speak("I'm not sure about, may be you should give me some time")
        
        elif "how are you" in query:
            speak("I'm fine, glad you me that")
 
        elif "i love you" in query:
            speak("It's hard to understand")

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")
        
        elif "open notepad" in query or "notepad" in query: 
            speak("Opening notepad") 
            os.startfile('C:\\Windows\\system32\\notepad.exe')

        elif "open word" in query or "ms word" in query or "open microsoft word" in query: 
            speak("Opening microsoft word") 
            os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Word 2007')

        elif "open powerpoint" in query or "ms powerpoint" in query or "open microsoft powerpoint" in query: 
            speak("Opening microsoft powerpoint") 
            os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office PowerPoint 2007')
        
        elif "open vs code" in query or "vs code" in query: 
            speak("Opening vs code for souvik") 
            os.startfile('C:\\Users\\Souvik Saha\\AppData\Local\Programs\\Microsoft VS Code\\Code.exe')

        # elif "open chrome" in query or "chrome" in query: 
        #     speak("Opening chrome for souvik") 
        #     os.startfile('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')
        # elif "close notepad" in query :
        #     os.system("taskkill /IM notepad.exe /F")
        elif 'volume up' in query or 'volumeup' in query:
            pyautogui.hotkey('volumeup')
        elif 'volume down' in query or 'volumedown' in query:
            pyautogui.hotkey('volumedown')
        elif 'volume mute' in query or 'mute' in query:
            pyautogui.hotkey('volumemute')
        elif 'open chrome' in query or 'chrome' in query:
            speak('openimg chrome boss , wait a second')
            pyautogui.hotkey('winleft')
            time.sleep(2)
            pyautogui.write('chrome' , 0.5)
            pyautogui.press('enter')
            pyautogui.hotkey('winleft')
        elif 'open' in query:
            query = query.replace("open", "")
            search = query
            print(f"opening {search}")
            speak(f"opening {search}")
            pyautogui.hotkey('winleft')
            time.sleep(2)
            pyautogui.write(search , 0.3)
            pyautogui.press('enter')



if __name__ == "__main__":
    while True:
        persmision = takeCommand()
        if "wake up" in persmision:
            task()
        elif "goodbye" in persmision:
            speak("thanks sir for using me")
            exit()
