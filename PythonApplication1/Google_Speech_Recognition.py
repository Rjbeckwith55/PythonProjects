import speech_recognition as sr
import time
#import brickpi3

#BP.brickpi3.BrickPi3()
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
            #BP.set_motor_position(BP.Port_A,45)
        elif word == "right":
            print("RIGHT")
            #BP.set_motor_position(BP.Port_A,-45)
        elif word == "shoot":
            print("SHOOT")
            #BP.set_motor_power(BP.Port_B,200)
            #time.sleep(.65)
            #BP.set_motor_power(BP.Port_B,0)
        elif word == "stop" or word == "quit" or word == "no":
            print("STOP")
            #BP.reset_all()
            break
        else:
            print("Not a command recognized by this program!")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    except KeyboardInterrupt:
        print("resetting all")
        #BP.reset_all()