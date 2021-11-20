import pytesseract
import mouse
import keyboard
import time
from PIL import ImageGrab

# Directory to pytesseract with ADMIN perms
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
)

#
# def afk_avoid():
#     screenshot2 = ImageGrab.grab(bbox=)
#     screenshot2.save("AFK_math.png")
#     text2 = str(pytesseract.image_to_string("AFK_math.png", config='--psm 7')).split()
#     if "AFK" in text2:
#         keyboard.press_and_release("k")
#         time.sleep(2)
#         keyboard.press_and_release("a")
#         keyboard.press("a")
#         time.sleep(0.1)
#         keyboard.press()
#

while True:
    screenshot = ImageGrab.grab(bbox=(500, 0, 1920, 110))
    screenshot.save("ECLIPSE.png")
    text = str(pytesseract.image_to_string("ECLIPSE.png", config='--psm 7')).split()
    print(text)

    if "reel" in text or "reel!" in text:
        keyboard.press_and_release("k")
        keyboard.press_and_release("i")
        mouse.move(865, 433, duration=0.5)
        mouse.click("right")
        mouse.move(922, 446, duration=0.5)
        time.sleep(10)
        mouse.click("left")
        keyboard.press_and_release("i")
