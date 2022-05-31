import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import pyjokes
import os

def speechtx():
    recognize = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listining...")
        recognize.adjust_for_ambient_noise(source)
        audio = recognize.listen(source)
        try:
            print("recogning...")
            data = recognize.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Not Understand")


def txspeech(x):
    engi = pyttsx3.init()
    voices = engi.getProperty('voices')
    engi.setProperty('voice', voices[1].id)
    rate = engi.getProperty('rate')
    engi.setProperty('rate', 130)
    engi.say(x)
    engi.runAndWait()

if __name__ == '__main__':

    # if "hello peter" in speechtx().lower():
        while True:
            data1 = speechtx().lower()

            if "your name" in data1:
                name = "my name is sara"
                txspeech(name)

            elif "old are you" in data1:
                age = "i am 2 days old"
                txspeech(age)

            elif "time now" in data1:
                time = datetime.datetime.now().strftime("%I%M%p")
                txspeech(time)

            elif "youtube" in data1:
                webbrowser.open("https://www.youtube.com/")

            elif "what's app" in data1:
                webbrowser.open("https://web.whatsapp.com/")

            elif "web" in data1:
                webbrowser.open("https://discord.com/channels/@me")

            elif "joke" in data1:
                joke_1 = pyjokes.get_joke(language='en', category='neutral')
                print( joke_1)
                txspeech(joke_1)

            elif "play song" in data1:
                address = "Music"
                listsong = os.listdir(address)
                print(listsong)

                os.startfile(os.path.join(address, listsong[0]))
            elif "exit" in data1:
                msg = "thank you"
                speechtx(msg)
                break

            # time.sleep(10)
    # else:
    #     print("thanks")