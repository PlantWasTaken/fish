from pynput.keyboard import Key, Controller
from PIL import Image, ImageGrab
from PIL import Image
from pixelmatch.contrib.PIL import pixelmatch
import pytesseract
import time as t

keyboard = Controller()
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
count = 0
x1,y1 = (394, 482) #screen
x2,y2 = (1061, 955) #screen

def fish():
    keyboard.type('/fish')
    t.sleep(0.1)
    keyboard.press(Key.space)
    t.sleep(0.1)
    keyboard.press(Key.enter)

def cap():
    def type(captcha):
        keyboard.type('/verify')
        t.sleep(0.3)
        keyboard.press(Key.space)
        t.sleep(0.3) 
        keyboard.type(captcha)
        t.sleep(0.3)
        keyboard.press(Key.enter)

    c_x1,c_y1 = (443, 795)
    c_x2,c_y2 = (623, 832)
    igmr = ImageGrab.grab(bbox=(c_x1,c_y1,c_x2,c_y2))
    igmr.save("cap.png")
    captcha_temp = (pytesseract.image_to_string('cap.png'))
    captcha = ""

    for i in captcha_temp:
        if(i == " " or i == "" or i == "\n"):
            pass
        else:
            captcha = captcha + i

    type(captcha)

    igmr = ImageGrab.grab(bbox=(x1,y1,x2,y2))
    igmr.save("Capture.png")
    text = (pytesseract.image_to_string('capture.png'))

    Done = False

    while Done == False:
        if("You may now continue." in text):
            Done = True
            pass
        else:
            type(captcha)
            t.sleep(5)

while True:
    igmr = ImageGrab.grab(bbox=(x1,y1,x2,y2))
    igmr.save("Capture.png")
    text = (pytesseract.image_to_string('capture.png'))

    if("You caught:" in text):
        print("fish")
        fish()
    elif("Anti-bot" in text):
        print("cap")
        cap()
    else:
        print("error")
        exit()

    t.sleep(3.7)
