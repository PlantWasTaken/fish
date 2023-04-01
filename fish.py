from pynput.keyboard import Key, Controller
from PIL import Image, ImageGrab
from PIL import Image
from pixelmatch.contrib.PIL import pixelmatch
import pytesseract
import time as t

keyboard = Controller()
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
count = 0

t.sleep(1) #5

def fish():
    global count
    keyboard.type('/fish')
    t.sleep(0.1)
    keyboard.press(Key.space)
    t.sleep(0.1)
    keyboard.press(Key.enter)
    print(count)
    count = count + 1

def fisherror():
    img_a = Image.open("fisherror.png")
    img_b = Image.open("TestFish.png")
    img_diff = Image.new("RGBA", img_a.size)
    mismatch = pixelmatch(img_a, img_b, img_diff, includeAA=True)
    return mismatch

def timererror():
    img_a = Image.open("timer.png")
    img_b = Image.open("TestFish.png")
    img_diff = Image.new("RGBA", img_a.size)
    mismatch = pixelmatch(img_a, img_b, img_diff, includeAA=True)
    return mismatch

def senderror():
    img_a = Image.open("send.png")
    img_b = Image.open("TestFish.png")
    img_diff = Image.new("RGBA", img_a.size)
    mismatch = pixelmatch(img_a, img_b, img_diff, includeAA=True)
    return mismatch

while True:
    x1,y1 = (384, 948) #fish 
    x2,y2 = (500, 981) #fish

    fish()

    t.sleep(2)
    #chapta detection / anyother detection / error detection
    igmr = ImageGrab.grab(bbox=(x1,y1,x2,y2))
    igmr.save("TestFish.png")

    img_a = Image.open("FISH.png")
    img_b = Image.open("TestFish.png")
    img_diff = Image.new("RGBA", img_a.size)
    mismatch = pixelmatch(img_a, img_b, img_diff, includeAA=True)

    t.sleep(1)
    if(mismatch != 0 and mismatch != 115):
        #capcha
        x1,y1 = (399, 877) 
        x2, y2 = (562, 911) 
        capcha = ImageGrab.grab(bbox=(x1,y1,x2,y2))
        capcha.save("cap.png")
        cap_temp = pytesseract.image_to_string('cap.png')
        cap = ""
        for i in cap_temp:
            if(i == " "):
                pass
            else:
                cap = cap + i

        #if error or captcha
        if(len(cap) == 6):
            print(cap)
            t.sleep(0.2)
            keyboard.type('/verify')
            t.sleep(0.2)
            keyboard.press(Key.space)
            t.sleep(0.2) 
            keyboard.type(cap)
            t.sleep(0.2)
            keyboard.press(Key.enter)
        else:
            t.sleep(1)
            fish()
        t.sleep(3)
    else:
        t.sleep(0.7) #3.5s total + 0.2 dleay
        t.sleep(0.3)
        pass
