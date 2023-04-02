from pynput.keyboard import Key, Controller
from PIL import Image, ImageGrab
import pytesseract
import time as t
import random
import cv2

keyboard = Controller()
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
count = 0
x1,y1 = (570, 263) #screen
x2,y2 = (1356, 936)
t.sleep(10)
def fish():
    keyboard.type('/fish')
    t.sleep(0.05)
    keyboard.press(Key.space)
    t.sleep(0.1)
    keyboard.release(Key.space)
    t.sleep(0.05)
    keyboard.press(Key.enter)
    t.sleep(0.1)
    keyboard.release(Key.enter)

def cap():
    def type_c(captcha):
        keyboard.type('/verify')
        t.sleep(0.3)
        keyboard.press(Key.space)
        t.sleep(0.3) 
        keyboard.release(Key.space)
        t.sleep(0.3)
        keyboard.type(captcha)
        t.sleep(random.randint(8,12))
        keyboard.press(Key.enter)
        t.sleep(0.3)
        keyboard.release(Key.enter)

    def cap_img():
        c_x1,c_y1 = (609, 762)
        c_x2,c_y2 = (852, 814)
        igmr = ImageGrab.grab(bbox=(c_x1,c_y1,c_x2,c_y2))
        igmr.save("cap.png")

    def solve_cap():
        captcha_image = cv2.imread('cap2.png')
        captcha_gray = cv2.cvtColor(captcha_image, cv2.COLOR_BGR2GRAY)
        captcha_dilated = cv2.dilate(captcha_gray, cv2.getStructuringElement(cv2.MORPH_RECT, (2,1)), iterations=1)
        captcha_text = pytesseract.image_to_string(captcha_dilated, config='--psm 10')
        captcha = ''

        for i in captcha_text:
            if(i == " "):
                pass
            else:
                captcha = captcha + i

        type_c(captcha)

    def verify_cap():
        igmr = ImageGrab.grab(bbox=(x1,y1,x2,y2))
        igmr.save("Capture.png")
        text = (pytesseract.image_to_string('capture.png'))
        if("You may now continue." in text or "You currently do not have an active captcha." in text):
            return True
        else:
            return False

    for i in range(3):     
        cap_img()
        t.sleep(5)
        solve_cap()
        t.sleep(5)
        if(verify_cap() == True):
            break
        else:
            type_c("regen")
        t.sleep(5)

    print("ERROR")
    exit()

while True:
    start_time = t.time()
    igmr = ImageGrab.grab(bbox=(x1,y1,x2,y2))
    igmr.save("Capture.png")
    text = (pytesseract.image_to_string('capture.png'))
    if("You caught:" in text or "LEVEL UP" in text or "You may now continue." in text or "You found an artifact box" in text or "You found a legendary crate" in text):
        fish()
    elif("Your cooldown" in text):
        t.sleep(3)
        fish()
    elif("Anti-bot" in text):
        print("cap")
        cap()
        t.sleep(1)
        fish()
    else:
        print("error")
        print(text)
        exit()
    t.sleep(2.2)
    print(t.time-start_time)
