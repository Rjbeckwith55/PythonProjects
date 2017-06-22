import time
from subprocess import call
import re
import brickpi3

#Function splits a big paragraph into smaller sentences for easy TTS
def splitParagraphIntoSentences(paragraph):
    sentenceEnders = re.compile('[.!?]')
    sentenceList = sentenceEnders.split(paragraph)
    return sentenceList

#Calls the Espeak TTS Engine to read aloud a sentence
#	er-ven+m7:	Male voice
#	-s180:		set reading to 180 Words per minute
#	-k20:		Emphasis on Capital letters
def sound(spk):
        cmd_beg=" espeak -ven+m7 -s180 -k20 --stdout '"
        cmd_end="' | aplay"
        print cmd_beg+spk+cmd_end
        call ([cmd_beg+spk+cmd_end], shell=True)

#Setting up the BrickPi for the page rotating arm
BP = brickpi3.BrickPi3()
roller = BP.PORT_B
speed_roller=100
speed_arm=100
arm = BP.PORT_C
BP.set_motor_power(roller,0)
sp=105
t1=.3
t2=.9

while True:
	#Take an image from the RaspberryPi camera with sharpness 100(increases the readability of the text for OCR)
	call ("raspistill -o j2.jpg -t 1 -sh 100", shell=True)
	print "Image taken"
	
	#Start the Tesseract OCR and save the text to out1.txt
	call ("tesseract j2.jpg out1", shell=True)
	print "OCR complete"
	
	#Open the text file and split the paragraph to Sentences
	fname="out1.txt"
	f=open(fname)
	content=f.read()
	print content
	sentences = splitParagraphIntoSentences(content)

	#Speak aloud each sentence in the paragraph one by one
	for s in sentences:
		sound(s.strip())
		
	#Move the motor arm to turn the page
	print "Next Page"
	BP.set_motor_power(roller, -speed_roller)
	ot = time.time()
	while(time.time() - ot < t1):    
		init_pos = BP.get_motor_encoder(arm)
		time.sleep(.1)          
	
	time.sleep(2)   
	BP.set_motor_power(roller, -55)
	BP.set_motor_power(arm, speed_arm) 

	#Rotate the arm to flip the page and stop at the initial position
	while True:			    
		if(BP.get_motor_encoder(arm)-init_pos>710):                    
			BP.set_motor_power(arm, -85)
			time.sleep(.1) 
			BP.set_motor_power(arm, 0)
			time.sleep(.01) 
			break
		time.sleep(.01)              # sleep for 100 ms
	
	#Move the roller to bring pages down
	time.sleep(2)   
	BP.set_motor_power(roller, 50)
	BP.set_motor_power(arm, 0)
	ot = time.time()
	while(time.time() - ot < 3):          
		time.sleep(.1)            
	time.sleep(3)
