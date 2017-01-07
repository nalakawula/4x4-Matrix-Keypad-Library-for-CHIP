from time import sleep
import keypad_4x4_lib_sumar

kp = keypad_4x4_lib_sumar.keypad()

digit_inputed = []

def digit():
	r = None
	while r == None:
		r = kp.getKey()
	return r

print ("Please enter a 4 digit code: ")

# Getting digit 1, printing it, then sleep to allow the next digit press.
d1 = digit()
print (d1)
sleep(1)

d2 = digit()
print (d2)
sleep(1)

d3 = digit()
print (d3)
sleep(1)

d4 = digit()
print (d4)

# printing out the assembled 4 digit code.
print ("You Entered %s%s%s%s "%(d1,d2,d3,d4))
