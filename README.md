# RaidMultiBattle
Another python autoclicker, this one has a similar usage to my PvZ sun picker, but this works on Raid Shadow Legends to make MultiBattle. for FREE!

To use it rightly, just run the fullscreen game on your pc while the program is running. Modify this line of python code according to the pixels of your game area (for example, using pyautogui.displayMousePosition in the python shell, I was able to determine the length and width of my screen, 2559x1439):

Line number 26: pic = pyautogui.screenshot(region=(0,0,[lenght],[width]))
