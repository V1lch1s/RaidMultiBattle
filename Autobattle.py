#Trabajo basado en el video https://youtu.be/YRAIUA-Oc1Y
#César Antonio Martínez Vilchis.

import pyautogui
import time
import keyboard
import random
import win32api, win32con #pywin32

#StartButton RGB: (229, 169,  14)
#Area X: 1402 Y: 1257 RGB: (20, 119, 150)
#Tamaño de interfaz: (2558, 1376)

#If your device has different dimensions change the values

time.sleep(2)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.001) #This pauses the script for 0.001 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    
while True:
    while keyboard.is_pressed('q') == False:
        pic = pyautogui.screenshot(region=(0,0,2559,1439))
        width, height = pic.size
        if pyautogui.locateOnScreen('startButton.png', confidence = 0.7) != None: # 0.7 equal to the presition of the image detected
            for x in range(0,width,5):
                for y in range(0,height,5):
                    r,g,b = pic.getpixel((x, y))
                    # Botón Empezar
                    if (r == 20 and g == 119 and b == 150):
                        click(x,y)
                        #pyautogui.moveTo(x,y) #To try the script
                        time.sleep(0.001)
                        break
                
    
print("Terminated\nPress Enter...")
input()
