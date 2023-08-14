#Aisha the assistant
import pyttsx3  # text to speech Convertion  library in python .
from datetime import datetime  #Combination of Date & Time.
import wikipedia  # it is a python Library that makes it easy to access and parse data from Wikipedia.
import webbrowser #it provides a high-level interface to allow displaying web-based documents to users.
import time #This module provides various time-related functions.
import os #The OS module in Python provides functions for interacting with the operating system. 
import re #used to perform Regular Expression Task.
from random import randint # used to generating random integers
import smtplib #for sending emails using the Simple Mail Transfer Protocol (SMTP).
import speech_recognition as sr  #Library for performing speech recognition, with support for several engines and APIs, online and offline.
import urllib #HTTP library with thread-safe connection pooling, file post, and more.
import playsound #it is cross platform, single function module with no dependencies for playing sounds.
import pyjokes # IT GIVES One line jokes for programmers
from urllib.request import urlopen


ass = pyttsx3.init()  #ass=object of pyttsx3 
my_gmail="swainsatya07@gmail.com"
mail = {"babu":"babubai39894@gmail.com"}

def is_net():
    try:
        urlopen("https://google.com",timeout=1)
        return True
    except :
        return False
def speak(audio) :
    vs = ass.getProperty('voices')  #now vs contains all volumes
    ass.setProperty("voice",vs[1].id)
    ass.setProperty("rate",150)
    ass.say(audio)
    ass.runAndWait()
def say(text):
    ass.say(text)
    ass.runAndWait()
#speak("enter name")
#a=input("enter name")
#speak("password")
#b=input("password")
#if a=="satyajit" and b=="satyajit1234":
	#print("valid customer")
	#speak("valid customer")
#speak("enter name")
#name=input("enter name")
#speak("enter password")
#pwd=input("enter password")
#while (name!="satyajit") or (pwd!="satyajit1234") :
#	speak("you have entered invalid name and password plz enter valid name and password")
#	print("plz enter valid name")
#	speak("enter valid name")
#	name=input("enter valid name")
#	speak("enter valid password")
#	pwd=input("enter password")
#speak("Thanks for conformation satyajit i am ready to help you")
#print("Thanks for confermation satyajit i am ready to help you")
	


def greet():
    hour = datetime.now().hour
    if hour>=5 and hour<12 :
        wish = "Good morning satyajit ! My self Aisha. I am your assistant ,how can i help you"
    elif hour >=12 and hour <17 :
        wish = "Good Afternoon satyajit ! My self Aisha. I am your assistant how can i help you"
    else :
        wish = "Good Evening dear satyajit ! My self Aisha. I am your assistant how can i help you"
    print (wish)
    speak(wish)
    
def takecommand():
    #it takes microphone input from the user and returns string output 
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print ("Listening....")
        speak ("listening") 
        r.energy_threshold=4500#minimium energy requered for recording
        r.pause_threshold=1#minimium wait for 1 second 
        audio = r.listen(source)
        try :
            print ("Recognizing..")
            cmd = r.recognize_google(audio)#
            print(cmd)
        except Exception as e:
            print("Sorry I could not understand Please repeat again ")
            speak("Sorry I could not understand Please repeat again ")
            cmd="-1"
    return cmd

def typecommand():
    speak("looking for your command")
    cmd=input("satyajit Please Enter your text please")
    return cmd

#print (mail["sandeep"])
greet()
if (is_net() == False):
    print("satyajit As You are not connected to the internet, so I cant recognize your voice")
    speak ("satyajit As You are not connected to the internet, so I cant recognize your voice")

while (True) :
    if (is_net()):
        query = takecommand().lower()
    else:
        query = typecommand().lower()

    if "wikipedia" in query :
        if (is_net()):
            result =wikipedia.summary(query,sentences=2)
            print ("Searching Please Wait ...")
            speak ("Searching Please Wait ...")
            query = query.replace("wikipedia","")
            speak ("According to wikipedia ")
            print (result)
            speak (result)
        else :
            print ("satyajit Can't connect to the internet at that moment")
            speak ("satyajit Can't connect to the internet at that moment")
            print ("Please check your connection then try again")
            speak ("Please check your connection then try again")

    elif  "open youtube" in query:
        if (is_net()):
            print ("Opening Youtube Please Wait ...")
            speak ("Opening Youtube Please Wait ...")
            webbrowser.open("youtube.com")
        else :
            print ("satyajit Can't connect to the internet at that moment")
            speak ("satyajit Can't connect to the internet at that moment")
            print ("Please check your connection then try again")
            speak ("Please check your connection then try again")


    elif "open google" in query:
        if (is_net()):
            print ("Opening Google Please Wait ...")
            speak ("Opening Google Please Wait ...")
            webbrowser.open("google.com")
        else :
            print ("satyajit Can't connect to the internet at that moment")
            speak ("satyajit Can't connect to the internet at that moment")
            print ("Please check your connection then try again")
            speak ("Please check your connection then try again")

    elif "open facebook" in query:
        if (is_net()):
            print ("Opening Facebook Please Wait ...")
            speak ("Opening Facebook Please Wait ...")
            webbrowser.open("facebook.com")
        else :
            print ("satyajit Can't connect to the internet at that moment")
            speak ("satyajit Can't connect to the internet at that moment")
            print ("Please check your connection then try again")
            speak ("Please check your connection then try again")

    elif "open gmail" in query:
        if (is_net()):
            print ("Opening Gmail Please Wait ...")
            speak ("Opening Gmail Please Wait ...")
            webbrowser.open("gmail.com")
        else :
            print ("satyajit Can't connect to the internet at that moment")
            speak ("satyajit Can't connect to the internet at that moment")
            print ("Please check your connection then try again")
            speak ("Please check your connection then try again")

    elif "play music" in query or "play song" in query or "play me a music" in query or "play a song" in query:
             print ("playing music for you")
             #speak ("playing {} for you".format(k))
             music="E://music"
             pl=os.listdir(music)
             r=randint(0,10)
             k=pl[r]
             def countdown(num):
             	print("count down started........")
             	speak("count down started........")
             	while num>0:
             		yield num
             		num=num-1
             v=countdown(3)
             for i in v:
             	print(i)
             	speak(i)
             	#time.sleep(1)
             speak("lets the music begin>>")
             print("playing {} for you".format(k))
             speak("playing {} for you".format(k))
             os.startfile(os.path.join(music,pl[r]))

    elif "play vedio" in query or "play vedio song" in query or "play me a vedio" in query or "play a vedio" in query:
             print ("playing music for you")
             #speak ("playing {} for you".format(k))
             music="E://music"
             pl=os.listdir(music)
             r=randint(0,10)
             k=pl[r]
             print("playing {} for you".format(k))
             speak("playing {} for you".format(k))
             os.startfile(os.path.join(music,pl[r]))


    elif "date and time" in query or "the date and time" in query or "the time and date" in query or "is time and date" in query:
        curr=datetime.now()
        #strDate = curr.strftime("%d. %B. %Y.")
        strDate = curr.strftime("%x")
        strTime = curr.strftime("%X")
        print ("satyajit, The Date is \n",strDate)
        speak ("satyajit, The Date is "+strDate)
        print ("satyajit, The time is, \n",strTime)
        speak ("satyajit, The time is, "+strTime)
    
    elif "is time" in query or "the time" in query:
        curr=datetime.now()
        strTime = curr.strftime("%X")
        print ("satyajit, The time is, \n",strTime)
        speak ("satyajit, The time is, "+strTime)
        
    elif "is date" in query or "the date" in query:
        curr=datetime.now()
        #strDate = curr.strftime("%d. %B. %Y.")
        strDate = curr.strftime("%x")
        print ("satyajit, The Date is \n",strDate)
        speak ("satyajit, The Date is "+strDate)
    elif "is day" in query or "the day" in query:
        curr=day.now()
        #strDate = curr.strftime("%d. %B. %Y.")
        strday = curr.strfday("%x")
        print ("satyajit, The Day is \n",strday)
        speak ("satyajit, The Day is "+strday)


    elif "open notepad" in query:
        print ("Opening notepad ...")
        speak ("Opening notepad ...")
        #os.startfile("C:\\Users\\HP\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\notepad")
        os.system("notepad")
     
    elif "open microsoft word" in query or "m s word" in query or "ms word" in query :
        print ("Opening Microsoft word...")
        speak ("Opening microsoft word...")
        os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\word")

    elif "open microsoft excel" in query or "m s excel" in query or "ms excel" in query :
        print ("Opening Microsoft excel...")
        speak ("Opening microsoft excel...")
        os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel")

    elif "open microsoft powerpaint" in query or "m s powerpaint" in query or "ms powerpaint" in query :
        print ("Opening Microsoft powerpaint...")
        speak ("Opening microsoft powerpaint...")
        os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\powerpoint")

    elif "open bigdata ppt" in query or "bigdata ppt" in query or "bigdata ppt" in query :
        print ("Opening bigdata ppt...")
        speak ("Opening bigdata ppt...")
        computernetwork= "E:\\computernetwork"
        p1=os.listdir(computernetwork)
        os.startfile(os.path.join(computernetwork,p1[1]))

    elif "introduce yourself" in query or "who are you" in query or "your introduction" in query or "about you" in query:
        print("satyajit My self Aisha")
        speak("satyajit My self Aisha")
        print("I am your assistant and I am here to help you")
        speak("I am your assistant and I am here to help you")
        print("what you have to do is just ask")
        speak("what you have to do is just ask")

    elif "i luve you" in query or "love u" in query or "love" in query :
    	a="it is 7th sense that destroy all the sense"
    	speak(a)
    	print(a)

    elif 'joke' in query: 
            speak(pyjokes.get_joke())
            print(pyjokes.get_joke()) 

    elif "don't listen" in query or "stop listening" in query: 
            speak("for how much time you want to stop aisha from listening commands") 
            a =int(takecommand())
            time.sleep(a)
            print(a)

    elif "write a note" in query: 
           speak("What should i write, sir") 
           note=takecommand() 
           file=open('aisha.txt', 'w') 
           speak("Sir, Should i include date and time") 
           snfm=takecommand()
           if 'yes' in snfm or 'sure' in snfm: 
               strTime=datetime.now()
               strTime=strftime("% H:% M:% S") 
               file.write(strTime) 
               file.write(" :- ") 
               file.write(note) 
           else: 
               file.write(note)
    elif "show note" in query: 
            speak("Showing Notes") 
            file = open("aisha.txt", "r")  
            print(file.read()) 
            speak(file.read(6)) 

    elif "open" in query :
    	reg_ex=re.search('open (.+)',query)
    	if reg_ex:
    		domain=reg_ex.group(1)
    		print(domain)
    		url='https://www.'+domain
    		webbrowser.open(url)
    		speak('the website you requested has been opened for you sir')
    	else:
    		pass
        
    elif "who made you" in query :
    	speak("i have been created by satyajit")

    elif "calculate" in query:
        k="enter first number"
        speak(k)
        a=input("enter first number")
        #speak("enter first no")
        speak("enter second number")
        b=input("enter second no")
        min=a if a<b else b
        print("the minimium value is: {}".format(min))
        speak("the minimium value is")
        speak(min)

    elif "expression" in query:
    	k="enter any expression"
    	speak(k)
    	a=input("enter any expression")
    	result=eval(a)
    	print("the result is",result)
    	speak("The result is")
    	speak(result)

    elif 'search' in query or 'play' in query: 
              
           query = query.replace("search", "")  
           query = query.replace("play", "")           
           webbrowser.open(query)
        

    elif "how are you" in query :
        print ("I am doing well,thankyou \nhow are you")
        speak ("I am doing well,thankyou . how are you")

    elif "fine" in query or "good" in query :
    	print("it's good to know you are fine")
    	speak("it's good to know you are fine")

    elif query is "-1":
         print("Sorry I could not understand Please repeat again ")
         speak("Sorry I could not understand Please repeat again")

    elif "your name" in query:
        print("My Self aisha")
        speak("My Self aisha.")
        print("And I am your assistant")
        speak ("And I am your assistant")

    elif "send mail" in query or "send a mail" in query or "send gmail" in query:
        if(is_net()):
            mail=smtplib.SMTP("smtp.gmail.com",587)
            mail.ehlo()
            mail.starttls()
            mail.login(my_gmail,"satyajitdas1798")
            print ("To whom")
            speak ("To whom")
            receiver=takecommand()
            mail.sendmail(my_gmail,"babubai39894@gmail.com","hey how are you")   
        else :
            print ("satyajit Can't connect to the internet at that moment")
            speak ("satyajit Can't connect to the internet at that moment")
            print ("Please check your connection then try again")
            speak ("Please check your connection then try again")

    elif "thanks" in query or "thankyou" in query:
        print("Your Welcome satyajit ,I am just doing my job")   
        
    elif "repeat" in query or "revice" in query:
        if (is_net()):
            text = takecommand().lower()
        else:
            text = typecommand().lower()
        print (text)
        speak (text)

    elif "exit" in query or "go" in query or "leave" in query or "shut up" in query or "get lost" in query:
        print ("ok satyajit")
        speak ("ok satyajit")
        print ("bye ! bye !")
        speak ("bye ! bye !")
        print ("i will happy to help u again Call me Again")
        speak ("i will happy to help u again Call me Again")
        exit()

    else :
        try :
            if (is_net()):
                results =wikipedia.summary(query,sentences=3)
                print ("Here are something matching with your text")
                speak ("According to wikipedia ")
                print (results)
                speak (results)
            else :
                print ("satyajit Can't connect to the internet at that moment")
                speak ("satyajit Can't connect to the internet at that moment")
                print ("Please check your connection then try again")
                speak ("Please check your connection then try again")

        except Exception as e:
            print("Sorry ! I  have a lot to learn")
            speak("Sorry ! I  have a lot. to learn")
    
        
    print ("What else can I do for you.")
    speak ("What else can I do for you")

   
