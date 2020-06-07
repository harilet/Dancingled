import pyaudio
import audioop
import serial,time
from tkinter import *
import threading


arduino = serial.Serial('COM7', 9600, timeout=.1)
time.sleep(2)

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 100
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

master = Tk()

Label(master,text="rate").grid(row=0,column=1)
Label(master,text="Offset").grid(row=0,column=2)

Label(master,text="red").grid(row=1,column=0)
DR = Scale(master, from_=0, to=255)
DR.grid(row=1,column=1)
DR.set(1)
OR = Scale(master, from_=0, to=255)
OR.grid(row=1,column=2)
OR.set(0)

Label(master,text="Green").grid(row=2,column=0)
DG = Scale(master, from_=0, to=255)
DG.grid(row=2,column=1)
DG.set(45)
OG = Scale(master, from_=0, to=255)
OG.grid(row=2,column=2)
OG.set(45)

Label(master,text="Blue").grid(row=3,column=0)
DB = Scale(master, from_=0, to=255)
DB.grid(row=3,column=1)
DB.set(45)
OB = Scale(master, from_=0, to=255)
OB.grid(row=3,column=2)
OB.set(45)

def audio1():
    while True:
        data = stream.read(CHUNK)
        rms = audioop.rms(data, 2)    # here's where you calculate the volume

        red=int((rms/DR.get())-OR.get()) if DR.get()!=0 else 0
        gre=int((rms/DG.get())-OG.get()) if DG.get()!=0 else 0
        blu=int((rms/DB.get())-OB.get()) if DB.get()!=0 else 0

        red = red if red < 255 else 255
        red = red if red >= 0 else 0
        if red>=255:
            gre = gre if gre < 255 else 255
            gre = gre if gre >= 0 else 0
            if gre>=255:
                blu = blu if blu < 255 else 255
                blu = blu if blu >= 0 else 0
            else:
                blu=0
        else:
            gre=0
            blu=0

        print(rms,":",red,":",gre,":",blu)
        str1=str(red)+" "+str(gre)+" "+str(blu)
        arduino.write(str1.encode('utf-8'))
        arduino.write(("\n").encode('utf-8'))


x=threading.Thread(target=audio1,args=())
x.start()
mainloop()

stream.stop_stream()
stream.close()
p.terminate()