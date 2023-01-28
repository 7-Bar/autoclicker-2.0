import pyautogui as pya
import time

thing = str(input("enter the thing that you want to spam: "))
wait = float(input("enter the time that you would want to pause between each spam: "))

while True:
    # make sure to enter your own coordinates here
    pya.click(1004, 529)
    pya.click(979, 860)
    
    pya.typewrite(thing)
    pya.press("enter")
    pya.press("enter")
    time.sleep(wait)
