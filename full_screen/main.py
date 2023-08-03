import time
import cv2
import pyautogui 
import numpy as np
import pyperclip
import pynput

img_file_path = "full_screen/img/"

nickname_frame = "name1"


def image_click(img_path, clicking = False, confidence = 0.95, delay = 0.1, dx = 0, dy = 0):
    while True:
        img_cap = pyautogui.locateOnScreen(img_file_path+img_path, confidence= confidence)
        if img_cap == None:
            if clicking:
                pyautogui.click()
            time.sleep(0.1)
            continue
        time.sleep(delay)
        pyautogui.moveTo(img_cap)
        pyautogui.moveRel(dx,dy)
        pyautogui.click()
        break

def REC(save_name = None):
    if save_name == None:
        save_name = "save"
        
    with pynput.keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
        listener.join()

    
def on_press(key):
    print('Key %s pressed' % key)

def on_release(key):
    print('Key %s released' %key)
    if key == pynput.keyboard.Key.esc:
        return False
        

if __name__ == "__main__":
    REC()