import serial,time
from tkinter import *
import threading
from tkinter.colorchooser import *

arduino = serial.Serial('COM7', 9600, timeout=.1)
time.sleep(2)

master = Tk()
Label(master,text="red").grid(row=0,column=0)
w1 = Scale(master, from_=0, to=255)
w1.grid(row=0,column=1)

Label(master,text="Green").grid(row=1,column=0)
w2 = Scale(master, from_=0, to=255)
w2.grid(row=1,column=1)

Label(master,text="Blue").grid(row=2,column=0)
w3 = Scale(master, from_=0, to=255)
w3.grid(row=2,column=1)

def getColor():
	color = askcolor()
	color=color[0]
	str1=""+str(int(color[0]))+" "+str(int(color[1]))+" "+str(int(color[2]))
	w1.set(int(color[0]))
	w2.set(int(color[1]))
	w3.set(int(color[2]))
	arduino.write(str1.encode('utf-8'))
	arduino.write(("\n").encode('utf-8'))
	data = arduino.readline()  # the last bit gets rid of the new-line chars
	if data:
		print(data)

Button(master,text='Select Color', command=getColor).grid(row=3,column=1)

def audio1():
    while True:

        red=w1.get()
        gre=w2.get()
        blu=w3.get()
        str1=str(red)+" "+str(gre)+" "+str(blu)
        arduino.write(str1.encode('utf-8'))
        arduino.write(("\n").encode('utf-8'))


x=threading.Thread(target=audio1,args=())
x.start()
mainloop()