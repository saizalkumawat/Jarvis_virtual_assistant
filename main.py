
import speech_recognition as sr  
import webbrowser
import pyttsx3 
import musiclibrary
import requests 
from openai import OpenAI
from gtts import gTTS
import pygame
import os

# pip install pocketsphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "< YOUR KEY HERE>"

def speak_old(text):
   engine.say(text)
   engine.runAndWait()

def speak(text):
   tts = gTTS(text)
   tts.save('temp.mp3')

# Initialize pygame mixer
   pygame.mixer.init()

# Load your MP3 file
   pygame.mixer.music.load('temp.mp3')

# Play the music
   pygame.mixer.music.play()

# Keep the program running until the music stops playing
   while pygame.mixer.music.get_busy():
      pygame.time.Clock().tick(10)

   pygame.mixer.music.unload()
   os.remove("temp.mp3")


def aiprocess(command):
   client = OpenAI(api_key="<YOUR_OPEN_API_KEY>",
   )

   completion = client.chat.completion.create(
   model="gpt-3.5-turbo",
   messages=[
        {"role":"sysyem","content": "you are a virtual assistant named jarvis sklilled in general tasks like alexa and google cloud. Give short responses please"},
        {"role": "user", "content": command}

   ]
   )
   return completion.choices[0].message.content

def processCommand(c):
   if "open google" in c.lower():
      webbrowser.open("https://google.com")
   elif "open linkedin" in c.lower():
      webbrowser.open("https://linkedin.com")
   elif "open facebook" in c.lower():
      webbrowser.open("https://facebook.com")
   elif "open youtube" in c.lower():
      webbrowser.open("https://youtube.com")
   elif c.lower().startswith("play"):
      song = c.lower().split(" ")[1]
      link = musiclibrary.music[song]
      webbrowser.open(link)

   elif "news" in c.lower():
      r = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
      if r.status_code == 200:
         #parse the JSON response
         data = r.json()
         # extract the articles
         articles = data.get('articles',[])
         #print the headlines
         for article in articles:
           speak(article['title'])
   else:
      #let OpenAI handle the request
      output = aiprocess(c)
      speak(output)

if __name__ == "__main__":
   speak("Initializing Jarvis....")
while True:
    # listen for the wake word "jarvis"
    #obtain audio from the microphone
    r= sr.Recognizer()


    print("recognising...")
    try:
      with sr.Microphone() as source:
        print("Listening....")
        audio = r.listen(source, timeout=3, phrase_time_limit=1)

      word = r.recognize_google(audio)
      if(word.lower()== "jarvis"):
         speak("ya")
      # listen for command

      with sr.Microphone() as source:
        print("Jarvis active...")
        audio = r.listen(source)
        command = r.recognize_google(audio)

        processCommand(command)


    except Exception as e:
      print("Error; {0}".format(e))