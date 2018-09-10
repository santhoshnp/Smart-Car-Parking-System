import RPi.GPIO as GPIO
import Tkinter
from Tkinter import *
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

root=Tkinter.Tk()
root.title("My app")
root.minsize(800, 800)
root.configure(bg = "blue")



count2=3
count_empty2=3

hall_entry=2
hall_exit=12
GPIO.setup(hall_entry,GPIO.IN)
GPIO.setup(hall_exit,GPIO.IN)

sound1 = 19
TRIG1 = 14                                 #Associate pin 23 to TRIG
ECHO1 = 15
 
sound2 = 26
TRIG2 = 16                           
ECHO2 = 20

ir1=17
ir2=27
ir3=22

led1=21
led2=6
led3=13

GPIO.setup(ir1,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(ir2,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(ir3,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
                                
GPIO.setup(sound1, GPIO.OUT)
GPIO.setup(sound2, GPIO.OUT)

GPIO.setup(TRIG1,GPIO.OUT)                  #Set pin as GPIO out
GPIO.setup(ECHO1,GPIO.IN)                   #Set pin as GPIO in

GPIO.setup(TRIG2,GPIO.OUT)                  #Set pin as GPIO out
GPIO.setup(ECHO2,GPIO.IN) 


l=Label(root, text = "Hello User")
l.pack()

T=Text(root, height=2, width=40)
T.pack()
T.insert(END, "SMART CAR PARKING SYSTEM")
	
if(count_empty2==3):
	T2=Text(root, height=2, width=40)
	T2.insert(END, "No of empty parking slots : "+str(count_empty2))	
	T2.pack()

def abc():

	global count2
	global count_empty2

	
	if GPIO.input(hall_entry):
		print "No car has entered"
	else:
		
		if(count_empty2>0 and count_empty2<4):
			print"Car has entered"
			count_empty2=count_empty2-1
			print "Total empty slots are now "+str(count_empty2)
			T3=Text(root, height=2, width=40)
			T3.insert(END, "No of empty parking slots : "+str(count_empty2))
			T3.insert(END, "\n")
			T3.pack()
			if (GPIO.input(ir1) and GPIO.input(ir2) and not(GPIO.input(ir3))):
				T6=Text(root, height=2, width=40)
				T6.insert(END, "No empty slot on left, 1 empty slot on right")
				T6.insert(END, "\n")
				T6.pack()	
			elif(GPIO.input(ir1) and GPIO.input(ir3) and not(GPIO.input(ir2))):
				T7=Text(root, height=2, width=40)
				T7.insert(END, "No empty slot on left, 1 empty slot on right")
				T7.insert(END, "\n")
				T7.pack()
			elif(GPIO.input(ir3) and GPIO.input(ir2) and not(GPIO.input(ir1))):
				T8=Text(root, height=2, width=40)
				T8.insert(END, "1 empty slot on left, no empty slot on right")
				T8.insert(END, "\n")
				T8.pack()
			elif(GPIO.input(ir3) and not(GPIO.input(ir2)) and not(GPIO.input(ir1))):	
				T9=Text(root, height=2, width=40)
				T9.insert(END, "1 empty slot on left, 1 empty slot on right")
				T9.insert(END, "\n")
				T9.pack()
			elif(GPIO.input(ir2) and not(GPIO.input(ir3)) and not(GPIO.input(ir1))):	
				T10=Text(root, height=2, width=40)
				T10.insert(END, "1 empty slot on left, 1 empty slot on right")
				T10.insert(END, "\n")
				T10.pack()
			elif(GPIO.input(ir1) and not(GPIO.input(ir2)) and not(GPIO.input(ir3))):	
				T11=Text(root, height=2, width=40)
				T11.insert(END, "No empty slots on left, 2 empty slots on right")
				T11.insert(END, "\n")
				T11.pack()
			elif(not(GPIO.input(ir1)) and not(GPIO.input(ir2)) and not(GPIO.input(ir3))):	
				T12=Text(root, height=2, width=40)
				T12.insert(END, "1 empty slot on left, 2 empty slots on right")
				T12.insert(END, "\n")
				T12.pack()
			elif(GPIO.input(ir1) and GPIO.input(ir2) and GPIO.input(ir3)):	
				T29=Text(root, height=2, width=40)
				T29.insert(END, "No empty slots")
				T29.insert(END, "\n")
				T29.pack()	
			
			if GPIO.input(hall_exit):
				print "No car has exited"
			else:
				if(count_empty2<3):
					print "1 car has exited"
					count_empty2=count_empty2+1
					T4=Text(root, height=2, width=40)
					T4.insert(END, "No of empty parking slots : "+str(count_empty2))
					T4.insert(END, "\n")
					T4.pack()
					print "Total empty slots are now "+str(count_empty2)
					if (GPIO.input(ir1) and GPIO.input(ir2) and not(GPIO.input(ir3))):
						T13=Text(root, height=2, width=40)
						T13.insert(END, "No empty slot on left, 1 empty slot on right")
						T13.insert(END, "\n")
						T13.pack()	
					elif(GPIO.input(ir1) and GPIO.input(ir3) and not(GPIO.input(ir2))):
						T14=Text(root, height=2, width=40)
						T14.insert(END, "No empty slot on left, 1 empty slot on right")
						T14.insert(END, "\n")
						T14.pack()
					elif(GPIO.input(ir3) and GPIO.input(ir2) and not(GPIO.input(ir1))):
						T15=Text(root, height=2, width=40)
						T15.insert(END, "1 empty slot on left, no empty slot on right")
						T15.insert(END, "\n")
						T15.pack()
					elif(GPIO.input(ir3) and not(GPIO.input(ir2)) and not(GPIO.input(ir1))):	
						T16=Text(root, height=2, width=40)
						T16.insert(END, "1 empty slot on left, 1 empty slot on right")
						T16.insert(END, "\n")
						T16.pack()
					elif(GPIO.input(ir2) and not(GPIO.input(ir3)) and not(GPIO.input(ir1))):	
						T17=Text(root, height=2, width=40)
						T17.insert(END, "1 empty slot on left, 1 empty slot on right")
						T17.insert(END, "\n")
						T17.pack()
					elif(GPIO.input(ir1) and not(GPIO.input(ir2)) and not(GPIO.input(ir3))):	
						T18=Text(root, height=2, width=40)
						T18.insert(END, "No empty slots on left, 2 empty slots on right")
						T18.insert(END, "\n")
						T18.pack()
					elif(not(GPIO.input(ir1)) and not(GPIO.input(ir2)) and not(GPIO.input(ir3))):	
						T19=Text(root, height=2, width=40)
						T19.insert(END, "1 empty slot on left, 2 empty slots on right")
						T19.insert(END, "\n")
						T19.pack()
					elif(GPIO.input(ir1) and GPIO.input(ir2) and GPIO.input(ir3)):	
						T27=Text(root, height=2, width=40)
						T27.insert(END, "No empty slots")
						T27.insert(END, "\n")
						T27.pack()
		
					
	if GPIO.input(hall_exit):
		print "No car has exited"
	else:
		if(count_empty2<3):
			print "1 car has exited"
			count_empty2=count_empty2+1
			T5=Text(root, height=2, width=40)
			T5.insert(END, "No of empty parking slots : "+str(count_empty2))
			T5.insert(END, "\n")
			T5.pack()
			print "Total empty slots are now "+str(count_empty2)
			if (GPIO.input(ir1) and GPIO.input(ir2) and not(GPIO.input(ir3))):
				T20=Text(root, height=2, width=40)
				T20.insert(END, "No empty slot on left, 1 empty slot on right")
				T20.insert(END, "\n")
				T20.pack()	
			elif(GPIO.input(ir1) and GPIO.input(ir3) and not(GPIO.input(ir2))):
				T21=Text(root, height=2, width=40)
				T21.insert(END, "No empty slot on left, 1 empty slot on right")
				T21.insert(END, "\n")
				T21.pack()
			elif(GPIO.input(ir3) and GPIO.input(ir2) and not(GPIO.input(ir1))):
				T22=Text(root, height=2, width=40)
				T22.insert(END, "1 empty slot on left, no empty slot on right")
				T22.insert(END, "\n")
				T22.pack()
			elif(GPIO.input(ir3) and not(GPIO.input(ir2)) and not(GPIO.input(ir1))):	
				T23=Text(root, height=2, width=40)
				T23.insert(END, "1 empty slot on left, 1 empty slot on right")
				T23.insert(END, "\n")
				T23.pack()
			elif(GPIO.input(ir2) and not(GPIO.input(ir3)) and not(GPIO.input(ir1))):	
				T24=Text(root, height=2, width=40)
				T24.insert(END, "1 empty slot on left, 1 empty slot on right")
				T24.insert(END, "\n")
				T24.pack()
			elif(GPIO.input(ir1) and not(GPIO.input(ir2)) and not(GPIO.input(ir3))):	
				T25=Text(root, height=2, width=40)
				T25.insert(END, "No empty slots on left, 2 empty slots on right")
				T25.insert(END, "\n")
				T125.pack()
			elif(not(GPIO.input(ir1)) and not(GPIO.input(ir2)) and not(GPIO.input(ir3))):	
				T26=Text(root, height=2, width=40)
				T26.insert(END, "1 empty slot on left, 2 empty slots on right")
				T26.insert(END, "\n")
				T26.pack()
			elif(GPIO.input(ir1) and GPIO.input(ir2) and GPIO.input(ir3)):	
				T28=Text(root, height=2, width=40)
				T28.insert(END, "No empty slots")
				T28.insert(END, "\n")
				T28.pack()
	
	

	current1 = GPIO.input(ir1)
	if current1==1 :
		GPIO.output(led1,True)
		print 'led1 '
		print 'ultrasonic1'
		GPIO.output(TRIG1, False)                 #Set TRIG as LOW
		print "Waiting For Sensor To Settle"
		time.sleep(1)                            #Delay of 2 seconds

  		GPIO.output(TRIG1, True)                  #Set TRIG as HIGH
  		time.sleep(0.00001)                      #Delay of 0.00001 seconds
  		GPIO.output(TRIG1, False)                 #Set TRIG as LOW

  		while GPIO.input(ECHO1)==0:               #Check whether the ECHO is LOW
  			pulse_start1 = time.time()              #Saves the last known time of LOW pulse

  		while GPIO.input(ECHO1)==1:               #Check whether the ECHO is HIGH
  			pulse_end1 = time.time()                #Saves the last known time of HIGH pulse 

  		pulse_duration1 = pulse_end1 - pulse_start1 
  		distance1 = pulse_duration1 * 17150      #Multiply pulse duration by 17150 to get distance
 		distance1 = round(distance1, 2)            #Round to two decimal points

  		if distance1 > 2 and distance1 < 400:      #Check whether the distance is within range
  			print "Distance1:",distance1 - 0.5,"cm"  #Print distance with 0.5 cm calibration

			if distance1<5:
				GPIO.output(sound1,True)
				print 'sound1 ringing'
			else:
				GPIO.output(sound1,False)
		
  		else:
  			print "Out Of Range"                   #display out
	if current1==0 :
		GPIO.output(led1,False)

	
	current2 = GPIO.input(ir2)
	if current2==1 :
		GPIO.output(led2,True)
		print 'led2'
		print 'ultrasoic2'
		GPIO.output(TRIG2, False)                 #Set TRIG as LOW
		print "Waiting For Sensor To Settle"
		time.sleep(2)                            #Delay of 2 seconds

  		GPIO.output(TRIG2, True)                  #Set TRIG as HIGH
  		time.sleep(0.00001)                      #Delay of 0.00001 seconds
  		GPIO.output(TRIG2, False)                 #Set TRIG as LOW

  		while GPIO.input(ECHO2)==0:               #Check whether the ECHO is LOW
  			pulse_start2 = time.time()              #Saves the last known time of LOW pulse

  		while GPIO.input(ECHO2)==1:               #Check whether the ECHO is HIGH
  			pulse_end2 = time.time()                #Saves the last known time of HIGH pulse 

  		pulse_duration2 = pulse_end2 - pulse_start2 
  		distance2 = pulse_duration2 * 17150      #Multiply pulse duration by 17150 to get distance
 		distance2 = round(distance2, 2)            #Round to two decimal points

  		if distance2 > 2 and distance2 < 400:      #Check whether the distance is within range
  			print "Distance2:",distance2 - 0.5,"cm"  #Print distance with 0.5 cm calibration

			if distance2<5:
				GPIO.output(sound2,True)
				print 'sound2 ringing'
			else:
				GPIO.output(sound2,False)
		
  		else:
  			print "Out Of Range" 
										
	if current2==0 :
		GPIO.output(led2,False)

	
	current3 = GPIO.input(ir3)
	if current3==1 :
		GPIO.output(led3,True)
		print 'led3'
		print 'No ultrasonic attached'
	if current3==0 :
		GPIO.output(led3,False)
			
	root.after(4000, abc)		

			
abc()


root.mainloop()
GPIO.cleanup()
