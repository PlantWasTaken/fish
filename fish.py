from pynput.keyboard import Key, Controller
from PIL import Image, ImageGrab
from PIL import Image
from pixelmatch.contrib.PIL import pixelmatch
import pytesseract
import time as t

keyboard = Controller()
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
x1,y1 = (384, 948)
x2,y2 = (500, 981)

t.sleep(5)
while True:
    keyboard.type('/fish')
    keyboard.press(Key.space)
    keyboard.press(Key.enter)
    t.sleep(2)
    #chapta detection / anyother detection
    igmr = ImageGrab.grab(bbox=(x1,y1,x2,y2))
    igmr.save("TestFish.png")
    img_a = Image.open("FISH.png")
    img_b = Image.open("TestFish.png")
    img_diff = Image.new("RGBA", img_a.size)
    mismatch = pixelmatch(img_a, img_b, img_diff, includeAA=True)


    if(mismatch != 0):
        #capcha
        x1,y1 = (399, 877) 
        x2, y2 = (562, 911) 
        capcha = ImageGrab.grab(bbox=(x1,y1,x2,y2))
        capcha.save("cap.png")
        cap_temp = pytesseract.image_to_string('cap.png')
        cap = ""
        for i in cap_temp:
            print(i)
            if(i == " "):
                pass
            else:
                cap = cap + i

        #if error or captcha
        if(cap == ''):
            pass
        else:
            keyboard.type('/verify')   
            keyboard.press(Key.space)   
            keyboard.type(cap)
            keyboard.press(Key.enter)
        
        t.sleep(3)
    else:
        t.sleep(1.25)
        pass


