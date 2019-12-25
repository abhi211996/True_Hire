import speech_recognition as sr
import pyaudio as pi
r = sr.Recognizer()

with sr.Microphone() as source:
    print("speak something")
    audio = r.listen(source)

    try:
       text= r.recognize_google(audio)
       print("you said:{}".format(text))

    except:
        print("sorry could not recognize your voice")

