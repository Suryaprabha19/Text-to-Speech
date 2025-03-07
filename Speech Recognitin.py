import pyttsx3
import speech_recognition as sr
import wikipedia
def speak(string):
    engine=pyttsx3.init()
    engine.say(string)
    engine.runAndWait()
def query():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)
        text=r.recognize_google(audio)
    return(text)
def search(string):
    return(wikipedia.summary(string,sentences=1))
speak("Say Something")
result=query().lower()
wiki_result=search(result)
speak(wiki_result) 
print(wiki_result)