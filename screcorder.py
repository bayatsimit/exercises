import os
import keyboard
import cv2
import numpy as np
import pyautogui #control mouse and keyboard

scrSize=tuple(pyautogui.size()) #get the screen size and convert it to a tuple firom size pbj
fourcc=cv2.VideoWriter_fourcc(*"XVID") 

count=0
while os.path.exists(f"output_{count}.avi"): #dont overwrite
    count+=1
out=cv2.VideoWriter(f"output_{count}.avi", fourcc, 12, (scrSize)) #fps=12

while True:
    ss=pyautogui.screenshot() #take a ss
    frame=cv2.cvtColor(np.array(ss), cv2.COLOR_BGR2RGB) #convert ss to np array and rgb
    out.write(frame) 

    if keyboard.is_pressed("q"):
        break

out.release()