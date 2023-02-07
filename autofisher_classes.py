import pytesseract
from PIL import ImageGrab
import mouse
import keyboard
import time


class AutoFish:
    def __init__(self):
        self.text = ""

    def read_text(self):
        """Snaps a screenshot of a specific resolution on the screen and reads the text in the screenshotted area"""

        # Directory to pytesseract with ADMIN perms
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

        screenshot = ImageGrab.grab(bbox=(500, 0, 1920, 110))
        screenshot.save("ECLIPSE.png")
        self.text = str(pytesseract.image_to_string("ECLIPSE.png")).split()
        print(self.text)

    def press_keys(self):
        """Simulates key presses when the activation text in """
        if "reel" in self.text or "reel!" in self.text:
            keyboard.press_and_release("k")
            keyboard.press_and_release("i")
            mouse.move(865, 433, duration=0.5)
            mouse.click("right")
            mouse.move(922, 446, duration=0.5)
            time.sleep(10)
            mouse.click("left")
            keyboard.press_and_release("i")

    def anti_afk(self):
        """Simulates key presses to avoid afk kick"""
        pass
