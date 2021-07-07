
from urllib.parse import quote
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
import winsound  
# import cv2
from selenium import webdriver
# from playsound import playsound
import winsound

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
def advice():
    url = 'https://www.boredapi.com/api/activity'
    response = requests.get(url)
    data = response.json()
    activity = data['activity']
    type = data['type']
    speak(f'if you are getting bored you can {activity} , and its a type of {type}...')



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
            time.sleep(10)
            pyautogui.click(x = 410, y =319 , button='left')
            time.sleep(8)
            pyautogui.click(x = 729, y =435 , button='left')
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
        elif 'exit' in query or 'goodbye' in query:
            speak('thank you for using me,sir')
            exit()
        elif 'stop listening' in query:
            speak("ok sir , its break time now")
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
            print("I'm fine, glad you me that")
 
        elif "i love you" in query:
            speak("It's hard to understand")
            print('it is hard to understand')

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")
        
        # elif "open notepad" in query or "notepad" in query: 
        #     speak("Opening notepad") 
        #     os.startfile('C:\\Windows\\system32\\notepad.exe')

        elif "open word" in query or "ms word" in query or "open microsoft word" in query: 
            speak("Opening microsoft word") 
            os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Word 2007')

        elif "open powerpoint" in query or "ms powerpoint" in query or "open microsoft powerpoint" in query: 
            speak("Opening microsoft powerpoint") 
            os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office PowerPoint 2007')
        
        elif "open vs code" in query or "vs code" in query: 
            speak("Opening vs code for souvik") 
            os.startfile('C:\\Users\\Souvik Saha\\AppData\Local\Programs\\Microsoft VS Code\\Code.exe')

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
            # pyautogui.hotkey('winleft')
        elif 'open' in query:
            query = query.replace("open", "")
            search = query
            print(f"opening {search}")
            speak(f"opening {search}")
            pyautogui.hotkey('winleft')
            time.sleep(2)
            pyautogui.write(search , 0.3)
            pyautogui.press('enter')
    
        elif 'take snapsort' in query or 'take screensort' in query:
            speak('taking screensort')
            im1 = pyautogui.screenshot()
            im1.save(r'C:\\Users\\Souvik Saha\\OneDrive\Desktop\\project\\screensort\\ss.png')
            speak('Done sir')
        elif 'can you give me any advice' in query or 'any suggestion' in query or 'advice' in query:
            query = query.replace('can you give me any' , "")
            query = query.replace('any suggestion' , "advice")
            speak(' well ! sir wait ')
            time.sleep(1)
            advice()
            print(advice())
        elif 'whats the weather mow' in query or 'weather' in query or 'current weather' in query or 'can you tell me the current weather' in query:
            query = query.replace('whats the weather mow' , "weather")
            query = query.replace('can you tell me the current weather' , "weather")
            chrome_path = 'E:\development\chromedriver.exe'
            city = speak('please tell me the city name , boss')
            print('please tell me the city name , boss')
            web = webdriver.Chrome(executable_path =chrome_path)
            web.get(f'https://openweathermap.org/find?q={city}')
            web1 = web.find_element_by_xpath('//*[@id="forecast_list_ul"]/table/tbody/tr/td[2]/p[1]')
            # speak(f'weather in {city} is ')
            speak(web1.text)
            print(web1.text)
            time.sleep(4)
            web.close()
        
        elif 'set a reminder' in query or 'set alarm' in query or 'alarm' in query:
            speak('sir , please tell me the hour , in 24 hours format')
            hour = takeCommand()
            speak('sir , please tell me the minute')
            mint = takeCommand()
            speak(f"alarm set at {hour} and {mint} minute")
            if datetime.datetime.now().hour == hour and datetime.datetime.now().minute == mint:
                speak("sir wake up")
                winsound.Beep(3000 , 10000)
            else:
                pass   
        elif 'facebook' in query or 'open facebook' in query:
            speak('opening facebook , wait a second')
            chrome_path = 'E:\development\chromedriver.exe'
            web = webdriver.Chrome(executable_path =chrome_path)
            web.get('https://www.facebook.com')
            web1 = web.find_element_by_name('email')
            web1.send_keys('')
            web2 = web.find_element_by_name('pass')
            web2.send_keys('')
            web3 = web.find_element_by_name('login')
            web3.click()
            time.sleep(10)
            web.close()
        elif 'introduce yourself' in query or 'tell me about yourself' in query:
            speak('hi sir , i am marshmellow. Souvik , indrani , Sabyasachi , Rounak have made me. currently I am learning.')




if __name__ == "__main__":
    while True:
        persmision = takeCommand()
        if "wake up" in persmision:
            task()
        elif "goodbye" in persmision:
            speak("thanks sir for using me")
            time.sleep(1)
            pyautogui.hotkey('ctrl' , 'c')

   
  