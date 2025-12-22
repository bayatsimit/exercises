import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

#vars
gap=0.01
bttn=Button.left

#keys
strtKey=KeyCode(char="s")
endKey=KeyCode(char="e")

#thread to run in the background so kb input doesnt get blocked
class Clicker(threading.Thread):#inherit Thread from threading
    def __init__(self, gap, bttn):
        super().__init__()#call constructor of the parent 
        self.gap=gap
        self.bttn=bttn
        self.clicking=False
        self.active=True #active as soon as created
        
    def strtClick(self):
        self.clicking=True
    def stpClick(self):
        self.clicking=False

    def exit(self):
        self.stpClick()
        self.active=False
    
    def run(self):
        while self.active:
            while self.clicking:
                mouse.click(self.bttn)
                time.sleep(self.gap)

#mouse controller instance
mouse=Controller()
autoclicker=Clicker(gap, bttn)
autoclicker.start()

#a func to listen to keyboard
def onPress(k):
    if k==strtKey:
        if autoclicker.clicking:
            autoclicker.stpClick()
            print("clicker stopped")
        else:
            autoclicker.strtClick()
            print("clicker clicking")
    elif k==endKey:
        autoclicker.exit()
        print("clicker exiting")
        return False
         
#start keyboard listener
with Listener(on_press=onPress) as listener:
    listener.join()
