from tkinter import *
import speech_recognition as sr
import webbrowser
import pyttsx3
from datetime import datetime
import subprocess

root = Tk()
root.geometry("500x500")
root.config(background = "Light Blue")

label = Label(root, text = "Welcome To Your Persoal Desktop Assistant", bg = "Light Blue", font = ("Banshrift Light", 15, "bold"))
label.place(relx = 0.5, rely = 0.1, anchor = CENTER)

text_to_speech = pyttsx3.init()
def speak(audio):
    text_to_speech.say(audio)
    text_to_speech.runAndWait()

def r_audio():
    speak("How can i help you..?")
    speech_recognisor = sr.Recognizer()
    with sr.Microphone() as source:
        audio = speech_recognisor.listen(source)
        voice_data=''
    try:
        voice_data= speech_recognisor.recognize_google(audio, language='en-in')
        
    except sr.UnknownValueError:
        print("Please repeat i did not get that")
        speak("Please repeat i did not get that")
        
    respond(voice_data)
    
def respond(voice_data):
    print(voice_data)
    if "name" in voice_data:
        speak("My name is Amol Kumar")
        print("My name is Amol Kumar")

    if "time" in voice_data:
        speak("Current time is ")
        now = datetime.now()
        Current_time = now.strftime("%H:%M:%S")
        speak(Current_time)
        print(Current_time)

    if "Google" in voice_data:
        speak("Opening Google")
        print("Opening Google")
        webbrowser.get().open("https://google.com")
        
    if "video" in voice_data:
        speak("Opening YouTube")
        print("Opening YouTube")
        webbrowser.get().open("https://youtube.com")
        
    if "notepad" in voice_data:
        speak("Opening The App")
        print("Opening The App")
        subprocess.Popen(["notepad.exe"])
        

btn = Button(root, text = "Start", command = r_audio, bg = "red3", fg = "white", padx = 10, pady = 1, font = ("Arial", 11, "bold"), relief = FLAT)
btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)

r_audio()

root.mainloop()