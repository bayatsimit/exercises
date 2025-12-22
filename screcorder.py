import cv2
import numpy as np
import pyautogui #control mouse and keyboard

scrSize=tuple(pyautogui.size()) #get the screen size and convert it to a tuple firom size pbj
fourcc=cv2.VideoWriter_fourcc(*"XVID") 
fps=12

out=cv2.VideoWriter(f"output.avi", fourcc, fps, (scrSize))
reqtime=5

for i in range(reqtime*fps): #for each frame
    ss=pyautogui.screenshot() #take a ss
    frame=cv2.cvtColor(np.array(ss), cv2.COLOR_BGR2RGB) #convert ss to np array and rgb
    out.write(frame)
    cv2.imshow("screenshoot", frame)
    if cv2.waitKey(1)==ord("q"):
        break

cv2.destroyAllWindows()
out.release()