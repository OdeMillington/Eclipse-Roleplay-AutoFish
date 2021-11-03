import pytesseract
import mouse
import keyboard
import time
from PIL import ImageGrab

# Directory to pytesseract with ADMIN perms
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
)


while True:
    screenshot = ImageGrab.grab(bbox=(500, 0, 1920, 110))
    screenshot.save("ECLIPSE.png")
    text = str(pytesseract.image_to_string("ECLIPSE.png", config='--psm 7')).split()
    print(text)

    if "reel" in text:
        keyboard.press_and_release("k")
        keyboard.press_and_release("i")
        mouse.move(865, 433, duration=0.5)
        mouse.click("right")
        mouse.move(922, 446, duration=0.5)
        time.sleep(10)
        mouse.click("left")
        keyboard.press_and_release("i")
