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
print(pytesseract.image_to_string('cap.png'))

t.sleep(5)
while True:
    keyboard.type('/fish ')
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
        keyboard.type('ABORT')
        keyboard.press(Key.enter)
        exit()
    else:
        t.sleep(1)
        pass


