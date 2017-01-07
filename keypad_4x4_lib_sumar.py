#!/usr/bin/python3
'''
keypad_4x4_lib_sumar.py
Module python untuk CHIP $9 Computer.
Merupakan module python untuk akses Keypad Matrix 4x4 yang dipasang pada CHIP.
Module ini dibuat karena setelah brwosing ternyata library matrix keypad untuk chip belum ada.
Modul ini membutuhkan pustaka CHIP_IO dari https://github.com/xtacocorex/CHIP_IO


Module ini dibuat dengan referensi dari:
https://www.raspberrypi.org/forums/viewtopic.php?t=81675&p=577225
https://pypi.python.org/pypi/matrix_keypad
'''

__author__ = "Sumarsono"

import CHIP_IO.GPIO as GPIO
from time import sleep

class keypad():
	def __init__(self):

		self.MATRIX = [[1,2,3,'A'],
			 [4,5,6,'B'],
			 [7,8,9,'C'],
			 ['*',0,'#','D']]

		self.ROW = ["XIO-P0","XIO-P2","XIO-P4","XIO-P6"]
		self.COL = ["XIO-P1","XIO-P3","XIO-P5","XIO-P7"]

		for j in range(4):
			GPIO.setup(self.COL[j], GPIO.OUT)
			GPIO.output(self.COL[j], 1)

		for i in range(4):
			GPIO.setup(self.ROW[i], GPIO.IN)


	def getKey(self):
		for j in range(4):
			GPIO.output(self.COL[j],0)

			for i in range(4):
				if GPIO.input(self.ROW[i]) == 0:
					#print (self.MATRIX[i][j])
					return self.MATRIX[i][j]
					sleep(0.2)
					while(GPIO.input(self.ROW[i]) == 0):
						pass
			GPIO.output(self.COL[j],1)

#if __name__ == '__main__':
	# Initialize the keypad class
#	kp = keypad()

	# Loop while waiting for a keypress
#	digit = None
#	while digit == None:
#		digit = kp.getKey()

#	# Print the result
#	print (digit)
