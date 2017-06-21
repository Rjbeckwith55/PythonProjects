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
#	-ven+m7:	Male voice
#	-s180:		set reading to 180 Words per minute
#	-k20:		Emphasis on Capital letters
def sound(spk):
        cmd_beg=" espeak -ven+m7 -s180 -k20 --stdout '"
        cmd_end="' | aplay"
        print cmd_beg+spk+cmd_end
        call ([cmd_beg+spk+cmd_end], shell=True)

#Setting up the BrickPi for the page rotating arm
BP = brickpi3.BrickPi3()
sp=105
t=.5

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
	'''BP.set_motor_power(BP.PORT_C,-sp) 	#Set the speed of MotorA (-255 to 255
	time.sleep(t)              # sleep for 100 ms
	BP.set_motor_power(BP.PORT_C,0) 
	time.sleep(.5)  
	BP.set_motor_power(BP.PORT_C,sp)  #Set the speed of MotorA (-255 to 255
	time.sleep(t)  '''