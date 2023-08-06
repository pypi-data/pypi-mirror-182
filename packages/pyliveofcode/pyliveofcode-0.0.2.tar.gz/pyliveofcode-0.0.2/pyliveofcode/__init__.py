import tkinter 
import random
import openai # pip install openai
from dotenv import load_dotenv #pip install python-dotenv
import pyttsx3 # pip install pyttsx3
import speech_recognition as sr # pip install SpeechRecognition==3.8.0
from googletrans import Translator # pip install googletrans
import webbrowser
fileopen = open("Api.txt","r")
API = fileopen.read()
fileopen.close()


openai.api_key = API
load_dotenv()
completion = openai.Completion()


def math(n1umber,operators,n2umber):
    if "+" in operators:
        print(int(n1umber)+int(n2umber))
    elif "-" in operators:
        print(int(n1umber)-int(n2umber))
    elif "*" in operators:
        print(int(n1umber)*int(n2umber))
    elif "/" in operators:
        print(int(n1umber)/int(n2umber))
    elif "%" in operators:
        print(int(n1umber)%int(n2umber))
    elif "**" in operators:
        print(int(n1umber)**int(n2umber))
    elif "//" in operators:
        print(int(n1umber)//int(n2umber))
def chatbot(question,botname,chat_log = None):
    FileLog = open("chat_log.txt","r")
    chat_log_template = FileLog.read()
    FileLog.close()
    if chat_log is None:
        chat_log = chat_log_template

    prompt = f'{chat_log}You : {question}\n'+(botname)+':'
    response = completion.create(
        model = "text-davinci-002",
        prompt=prompt,
        temperature = 0.5,
        max_tokens = 60,
        top_p = 0.3,
        frequency_penalty = 0.5,
        presence_penalty = 0)
    answer = response.choices[0].text.strip()
    chat_log_template_update = chat_log_template + f"\nYou : {question} \n"+botname+":"+answer
    FileLog = open("chat_log.txt","w")
    FileLog.write(chat_log_template_update)
    FileLog.close()
    return answer
def makepassword():
    passwordmaker = random.random()
    float(passwordmaker)
    str(passwordmaker)
    print("here is the password sir:",passwordmaker)
    print("sir 0. is not in the password")
    password =passwordmaker
def makefile(dx,name,ex):
    fileopen1 = open(dx+name+ex,"w")
    fileopen1.close
def write(text):
    print(text)

def Listen(languagename):

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,8) # Listening Mode.....
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language=languagename)

    except:
        return ""
    
    query = str(query).lower()
    return query
def Speak(Text):
     engine = pyttsx3.init("sapi5")
     voices = engine.getProperty('voices')
     engine.setProperty('voice',voices[0].id)
     engine.setProperty('rate',170)
     engine.say(Text)
     engine.runAndWait()
def Translatortext(text,languagenameoftranslator):
    line = str(text)
    translate = Translator()
    result = translate.translate(line,languagenameoftranslator)
    data = result.text
    print(data)
    return data
def inputtofile(dx,inputsreen):
    input1 = input(inputsreen)
    d=open(dx,"w")
    d.write(input1)
    d.close()
# Api Key
fileopen = open("Api.txt","r")
API = fileopen.read()
fileopen.close()

# Importing
import openai
from dotenv import load_dotenv

#Coding

openai.api_key = API
load_dotenv()
completion = openai.Completion()

def QuestionsAnswer(question,chat_log = None):
    FileLog = open("qna_log.txt","r")
    chat_log_template = FileLog.read()
    FileLog.close()
    if chat_log is None:
        chat_log = chat_log_template

    prompt = f'{chat_log}Question : {question}\nAnswer : '
    response = completion.create(
        model = "text-davinci-002",
        prompt=prompt,
        temperature = 0,
        max_tokens = 100,
        top_p = 1,
        frequency_penalty = 0,
        presence_penalty = 0)
    answer = response.choices[0].text.strip()
    chat_log_template_update = chat_log_template + f"\nQuestion : {question} \nAnswer : {answer}"
    FileLog = open("qna_log.txt","w")
    FileLog.write(chat_log_template_update)
    FileLog.close()
    return answer
def search(url):
    webbrowser.open("https://www.google.com/search?q="+url)
def searchwebsite(url):
    webbrowser.open_new_tab(url)
