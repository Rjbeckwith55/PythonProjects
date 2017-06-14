import time
import socket 
import brickpi3

BP.brickpi3.BrickPi3()
word = ''
PORT=9500
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', PORT))
s.listen(1)
s.setsockopt(socket.IPPROTO_TCP , socket.TCP_NODELAY , 1 )
conn, addr = s.accept()

# Record Audio
while word != "STOP":
# Speech recognition using Google Speech Recognition
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")
    word = conn.recv(6).decode()
    print("You said: " + word)
    if word == "left":
        print("LEFT")
        BP.set_motor_position(BP.Port_A,45)
    elif word == "right":
        print("RIGHT")
        BP.set_motor_position(BP.Port_A,-45)
    elif word == "shoot":
        print("SHOOT")
        BP.set_motor_power(BP.Port_B,200)
        time.sleep(.65)
        BP.set_motor_power(BP.Port_B,0)
    elif word == "STOP":
        print("STOP")
        BP.reset_all()
        break
    else:
        print("Not a command recognized by this program!")
