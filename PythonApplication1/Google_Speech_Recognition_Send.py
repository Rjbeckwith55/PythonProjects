import speech_recognition as sr
import time
import socket

HOST = '192.168.1.138'
PORT = 9500
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print("Connection to " + HOST + " was successful")

word = ''
# Record Audio
while word != "quit":
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
 
    # Speech recognition using Google Speech Recognition
    try:
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        word = r.recognize_google(audio)
        print("You said: " + word)
        if word == "left":
            print("LEFT")
            word = word.encode()
            s.send(word)
        elif word == "right":
            print("RIGHT")
            word = word.encode()
            s.send(word)
        elif word == "shoot":
            print("SHOOT")
            word = word.encode()
            s.send(word)
        elif word == "stop" or word == "quit" or word == "no":
            word = "STOP"
            print(word)
            word = word.encode()
            s.send(word)
            break
        else:
            print("Not a command recognized by this program!")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    except KeyboardInterrupt:
        print("resetting all")