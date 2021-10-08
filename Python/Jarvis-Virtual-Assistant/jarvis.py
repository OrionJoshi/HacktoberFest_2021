import pyttsx3
from pywhatkit.mainfunctions import shutdown
from requests.api import head #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import requests
import random
import cv2
import pywhatkit as kit
import sys
import pyjokes
import os
import smtplib
import pyautogui
import time
import instaloader
import PyPDF2
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import QTimer, QTime,QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvisUI import Ui_MainWindow
from pywikihow import *
import psutil
import speedtest
import twilio
from twilio.rest import Client
import wolframalpha

try:
    
    app_id = wolframalpha.Client("UXQR8Q-JXLTP773AQ")

except Exception:
    print("Some features are not wrking")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def news():

    main_url="https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=47f1311cf2704a85a72927ed4706e097"
    main_page=requests.get(main_url).json()
    #print(main_page)
    articles=main_page["articles"]
    head=[]
    day=["first","second","third"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")



def pdf_reader(): #pdf reader is not working properly
    book = open('think.pdf','rb')
    pdfReader= PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    #speak(f"Total number of pages in this book {pages}")
    #speak("sir please enter the page number I have to read")
    #pg = int (input("Please enter the page number:"))

    #pg=7
    page = pdfReader.getPage(7)
    text = page.extractText()
    print("Playing the audiobook")
    '''for num in range(0,pages):
        page = pdfReader.getPage(num)
        Data = page.extractText()
        print(Data)
        speak(Data)'''
    return text

def computational_intelligence(question):
    try:
        client = wolframalpha.Client(app_id)
        answer = client.query(question)
        answer = next(answer.results).text
        print(answer)
        return answer
    except:
        speak("Sorry sir I couldn't fetch your question's answer. Please try again ")
        return None  
    
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremailaddr@gmail.com', 'password')
    server.sendmail('youremailaddr@gmail.com', to, content)
    server.close()

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.TaskExecution()

    def takeCommand(self):
        #It takes microphone input from the user and returns string output

        r=sr.Recognizer()
        #print(sr.Microphone.list_microphone_names())
        with sr.Microphone() as source:
            
            # r.energy_threshold()
            print("Listening: ")
            r.pause_threshold=1
            audio= r.listen(source,timeout=5,phrase_time_limit=8)
            try:
                print("Recognizing")
                query = r.recognize_google(audio,language='en-in')
                print(f"User Said : {query}")
            except Exception as e:
                speak("say that again please")
                return "none"
            return query

    def TaskExecution(self):

        wishMe()
        while True:
        # if 1:
            self.query = self.takeCommand().lower()

            # Logic for executing tasks based on query
            if 'wikipedia' in self.query:
                speak('Searching Wikipedia...')
                query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in self.query:
                speak("opening youtube")
                webbrowser.open("youtube.com")

            elif  'command prompt' in self.query:
                    out='Opening Command Prompt'
                    speak(out)
                    path = r'C:\Windows\System32\cmd.exe'
                    os.startfile(path)

            
            

            elif 'open browser' in self.query:
                speak("sir, what should I search on google ?")
                cm = self.takeCommand().lower()
                
                webbrowser.open(f"{cm}")

            elif 'open stackoverflow' in self.query:
                webbrowser.open("stackoverflow.com")  

            elif 'open google' in self.query:
                webbrowser.open("google.com")  


            elif 'open facebook' in self.query:
                webbrowser.open("facebook.com")   

            elif 'open instagram' in self.query:
                webbrowser.open("instagram.com")   

            


            elif 'play music' in self.query:
                speak("playing music")
                music_dir = r'C:\Users\DELL\Music\fav_songs'
                songs = os.listdir(music_dir)
                #print(songs)    
                os.startfile(os.path.join(music_dir, songs[0]))

            elif 'play movies' in self.query:
                speak("playing movies")
                music_dir = r'D:\Ent'
                songs = os.listdir(music_dir)
                print(songs)    
                os.startfile(os.path.join(music_dir, songs[0]))

            elif 'send message' in self.query:
                speak("What should I say?")
                msz = self.takeCommand()
                account_sid = os.environ['ACb7b53be70304d7e06a2c524742caa240']
                auth_token = os.environ['935f6f600a256c8ae0c6d4b41d10365a']
                client = Client(account_sid, auth_token)

                message = client.messages \
                .create(
                    body='This is the ship that made the Kessel Run in fourteen parsecs?',
                    from_='+15416405052',
                    to='+123456789'
                )

                print(message.sid)
            

            elif 'the time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"Sir, the time is {strTime}")

            elif 'open code' in self.query:
                speak("opening visual studio code")
                codePath = r"C:\Users\DELL\AppData\Local\Programs\Microsoft VS Code\Code.exe"
                os.startfile(codePath)

            
            elif 'current' in self.query:            
                    out='Opening Current Working Directory'                                                     
                    
                    speak(out)
                    path = ''
                    os.startfile(path)

            elif 'python' in self.query:
                    out='Opening Python'
                    
                    speak(out)
                    path = r'C:\Users\DELL\PycharmProjects\V_A\venv\Scripts\python.exe'
                    os.startfile(path)

            elif 'paint' in self.query:
                    out='Opening Paint'
                    
                    speak(out)
                    os.chdir(r'C:\Windows\system32')
                    #os.chdir(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories')
                    path = r'C:\Windows\system32\mspaint.exe'
                    os.startfile(path)
          

            elif 'wordpad' in self.query:
                    out='Opening WordPad'
                    
                    speak(out)
                    path = r'C:\Program Files\Windows NT\Accessories\wordpad.exe'
                    os.startfile(path)

            elif 'open notepad' in self.query:
                    out='Opening Note Pad'
                    
                    os.chdir(r'C:\Windows\system32')
                    speak(out)
                    path = r'C:\Windows\system32\notepad.exe'
                    os.startfile(path)

            elif 'r studio' in self.query:
                    out='Opening R Studio'
                    
                    os.chdir(r'C:\Program Files\RStudio\bin')
                    speak(out)
                    path = r'C:\Program Files\RStudio\bin\rstudio.exe'
                    os.startfile(path)

            elif 'snake' in self.query:
                    out='Opening Snake Game'
                    
                    speak(out)
                    path = r'C:\Users\DELL\Desktop\Raw Data\snake_game.py'
                    os.startfile(path)

            elif 'calculator' in self.query:
                    out = 'Opening Calculator'
                    
                    os.chdir(r'C:\Windows\System32')
                    speak(out)
                    path = r'C:\Windows\System32\calc.exe'
                    os.startfile(path)

            elif 'sticky notes' in self.query:
                    out = 'Opening Sticky Notes'
                    
                    os.chdir(r'C:\Windows\System32')
                    speak(out)
                    path = r'E:\EXE_FILES\STICKY_NOTES.exe'
                    os.startfile(path)

            elif 'launch' in self.query or 'chrome' in self.query:
                    out = 'launching Crome Browser'
                
                    speak(out)
                    path = r'C:\Users\DELL\AppData\Local\Google\Chrome\Application\chrome.exe'
                    os.startfile(path)

            elif 'take screenshot' in self.query or 'take a screenshot' in self.query:
                    speak("sir , please tell me the name for this screenshot file")
                    name=self.takeCommand().lower()
                    speak("please hold the screen for few seconds, i am taking screenshot")
                    time.sleep(3)
                    img = pyautogui.screenshot()
                    img.save(f"{name}.png")
                    speak("I am done sir, the screenshot is saved in our main folder. now I am ready for take commands")

             

            elif 'activate how to do mode' in self.query:   

                speak("How to do mode is activated please tell me what you want to know")
                how = self.takeCommand()
                max_results = 1
                how_to = search_wikihow(how,max_results)
                assert len(how_to) == 1
                #how_to[0].print()
                #results = wikipedia.summary(query, sentences=2)
                speak(how_to[0],summary)            

            elif "internet speed" in self.query:
                st= speedtest.Speedtest()
                dl = st.download()
                up = st.upload()
                speak(f"sir we have {dl} bit per second downloading speed and {up} bit per second uploading speed")             

            elif 'picture' in self.query or 'images' in self.query or 'photo' in self.query:
                    out = 'Opening  Images'
                    
                    speak(out)
                    path = r'C:\Users\DELL\Pictures\Screenshots'
                    os.startfile(path)
            #Tell a joke
            
            elif 'shutdown the system' in self.query:
                os.system("shutdown /s /t 5")

            elif "restart the system" in self.query:
                os.system("shutdown /r /t 5")
            elif "sleep the system" in self.query:
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            
            #To set an alarm
            elif 'set alarm' in self.query:
                nn = int(datetime.datetime.now().hour)
                if nn==22:
                    music_dir =r"C:\Users\DELL\Music\arjit"
                    songs = os.listdir(music_dir)
                    os.startfile(os.path.join(music_dir,songs[0]))

            elif 'tell me joke' in self.query:
                joke = pyjokes.get_joke()
                speak(joke)

            

            #-----------------------------Weather CONDITION--------------------------------------------------------------------------------
            elif  'weather' in self.query:
                try:
                    if 'in' in self.query:
                        u = self.query.split()
                        for i in range(0,len(u)):
                            if u[i] == 'in':
                                city = u[i+1]
                            
                        api='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
                        url = api+city
                        json_data = requests.get(url).json()
                        format_add = json_data['weather'][0]['main']
                        format_temp = json_data['coord']['lat']
                        out = f'Temperture In {city} is {format_temp} Deegre Celcius, And Climate is {format_add}'
                        print(out)
                        speak(out)
                        
                    else:
                        url='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q=Ludhiana'                            
                        json_data = requests.get(url).json()
                        format_add = json_data['weather'][0]['main']
                        format_temp = json_data['coord']['lat']
                        out = f'Temperture In Your city is {format_temp} Deegre Celcius, And Climate is {format_add}'
                        print(out)
                        speak(out)
                except:
                    out = 'I Was Unable To Connect To Internet.'
                    print(out)
                    speak(out)
            #------------------------------
            
            elif 'where' in self.query and 'i' in self.query or 'location' in self.query:
                try:
                    r = requests.get('https://ipinfo.io/')
                    d = r.text.split()[4]
                    out='You Location Is Near To ' + d
                    print(out)
                    speak(out)
                except:
                    out='I Was Unable To Track Your Location'
                    print(out)
                    speak(out)

            elif 'how are you' in self.query:                               #|
                    speak("I am fine sir!")                                            #|
                    print("I am fine sir")    
            
            elif 'who made you' in self.query:
                    out="I was made by Madhuri"
                    speak(out)
                    print(out)
            elif 'can we become friends' in self.query:
                    out="Yes of course ! It will be great pleasure for me to become your friend"
                    speak(out)
                    print(out)
            elif 'tell me about yourself' in self.query:
                    out="I am Jarvis mam . I am your virtual assistant !"
                    speak(out)
                    print(out)

            #----To check a  instagram profile
            elif 'instagram profile' in self.query or 'profile on instagram' in self.query:
                    speak("sir enter the username correctly.")
                    name= input("Enter username here : ")
                    webbrowser.open(f"www.instagram.com/{name}")
                    speak(f"sir here is the profile of user {name}")
                    time.sleep(5)
                    speak("Sir would you like to download profile picture of this account?")
                    condition = self.takeCommand().lower()
                    if 'yes' in condition:
                        mod = instaloader.Instaloader()
                        mod.download_profile(name,profile_pic_only=True)
                        speak("I am done sir, profile picture is saved in our main folder. now I an ready to take commands")

                    else:
                        pass

            #To close any application
            elif 'close notepad' in self.query:
                speak("okay sir closing notepad")
                os.system("taskkill /f /im notepad.exe")
            
            elif 'send message' in self.query:
                kit.sendwhatmsg("+7218394712","Hello Madhuri ..",2,25)

            elif 'play songs on youtube' in self.query:
                kit.playonyt("see you again")

            elif 'you can sleep' in self.query:
                speak("Thanks for using me, Have a good day")
                sys.exit()

            #--to hide all files
           
                    

            elif "switch the window" in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")

            elif "tell me news" in self.query:
                speak("Please wait sir , fetching the latest news")
                news()

            elif 'read pdf' in self.query:
                data=pdf_reader()
                speak(data)

            

            

            elif 'open camera' in self.query:
                    cap = cv2.VideoCapture(0)
                    while True:
                        ret, img = cap.read()
                        cv2.imshow('webcam',img)
                        k = cv2.waitkey(50)
                        if k==27:
                            break
                        
                    cap.release()
                    cv2.destroyAllWindows()
            elif 'how much battery we have left' in self.query or 'battery' in self.query:
                battery = psutil.sensors_battery()
                percentage = battery.percent
                speak(f" sir our system have {percentage} percent battery")

            elif "calculate" in self.query:
                try:
                    res = app_id.query(self.query)
                    print(next(res.results).text)
                    speak(next(res.results).text)
                except:
                    print("Internet connection error")
                    speak("Internet connection error")
                
            
            elif "what is" in self.query or "who is" in self.query:
                try:
                    res = app_id.query(self.query)
                    print(next(res.results).text)
                    speak(next(res.results).text)
                except:
                    print("Internet connection error")
                    speak("Internet connection error")

            

            elif 'email to mayuri' in self.query:
                try:
                    speak("What should I say ?")
                    content = self.takeCommand().lower()
                    to = "youremail@gmail.com"
                    sendEmail(to,content)
                    speak("Email has been sent to mayuri" )
                except:
                    print(e)
                    speak("Sorry sir I am not able to send this email")
                


           
                    

        

        
                

                   
                       
                
                                               #|

startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("jimage.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("init.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date= QDate.currentDate()
        label_time = current_time.toString("hh:mm:ss")
        label_date =current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)


app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())