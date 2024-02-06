import numpy as np
import pytesseract
import cv2
import pyscreenshot as ImageGrab
import time
import PIL 
import datetime
import pyautogui
import warnings
import win32api


warnings.filterwarnings('ignore')




#sözlük gibi bişey yap buraya
    
Battle = cv2.imread('Battle.png', cv2.TM_CCOEFF_NORMED)
Defeat = cv2.imread('Defeat.png', cv2.TM_CCOEFF_NORMED)
No_gold = cv2.imread("no_gold.png", cv2.TM_CCOEFF_NORMED)
archer = (1410,410)
tower = (1410,310)
battle_button = (1530,890)
replay = (1345,890)
middle = (1345,890)




def ask(arr):
    
    img=ImageGrab.grab(bbox=(213,160,1635,960))
    full = np.array(img)
    
    result = cv2.matchTemplate(full, arr, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    
    if max_val >= 0.7:
        return True
    else:
        return False
    


def Passed(now1):
    
    now2 = datetime.datetime.now()
    passed = (now2-now1)
    sec = passed.total_seconds()/60
    return sec

def Click(x,y,right=0,delay=0.5):
    if right==0:        
        pyautogui.moveTo(x, y,delay)
        time.sleep(delay)
        pyautogui.click()
    if right==1:
        
        pyautogui.moveTo(x, y,delay)
        time.sleep(delay)
        pyautogui.click(button='right')
        
    

#%%



def action1(counter):
    Click(archer[0],archer[1])        
    counter = counter +1     
    return counter     

def action2(counter):
    Click(tower[0],tower[1])        
    counter = counter +1     
    return counter    

def upgrade():
    state="upgrade"
    print(state)
    counter=0
    while True:
        if counter <=20:
            counter=action1(counter)
        else:
            counter=action2(counter)
        if counter ==25:
            counter =0
        if ask(No_gold)==True:
            break
                                        
                    
def fight():
    state="fight"
    print(state)
    while True:
        time.sleep(0.5)
        if ask(Defeat)==True:
            break
        if ask(Battle) ==True:
            Click(battle_button[0],battle_button[1])
    
            
def farm():
    state="farm"
    print(state)
    now1 = datetime.datetime.now()
    while Passed(now1) < 3600:
        Click(replay[0],replay[1])
        time.sleep(1)
        Click(middle[0],middle[1])
        
def Play():
    time.sleep(5)
    while True:
        
        upgrade()
        fight()
        farm()

 
   
Play()

"""
import cv2
import time


cap = cv2.VideoCapture("vid.mp4")

# Object detection from Stable camera
object_detector = cv2.createBackgroundSubtractorMOG2()
while True:
    time.sleep(0.1)
    ret, frame = cap.read()
   
    # 1. Object Detection
    mask = object_detector.apply(frame)
    cont,_=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for cnt in cont:
        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow("Frame",frame)
    
    key=cv2.waitKey(30)
    if key ==27:
        break
    
cv2.destroyAllWindows()


"""


