import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

#pip install pocketsphinix

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "google kholo" in c.lower():
        webbrowser.open("https://google.com")
    elif "facebook kholo" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "youtube kholo" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "linkedin kholo" in c.lower():
        webbrowser.open("https://linkedin.com")
   
    elif c.lower().endswith("bolo"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

if __name__ == "__main__":
    speak("Novo aagaya....")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "novo"):
                speak("Bolo")
                # Listen for command
                with sr.Microphone() as source:
                    print("Novo Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)


        except Exception as e:
            print("Error; {0}".format(e))