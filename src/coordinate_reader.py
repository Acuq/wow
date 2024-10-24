import pyautogui
import easyocr
import numpy as np

class CoordinateReader:
    def __init__(self):
        self.reader = easyocr.Reader(['en'])

    def current_char_position(self):
        current_x_screen = pyautogui.screenshot(region=(918, 4, 85, 25))
        current_y_screen = pyautogui.screenshot(region=(918, 35, 85, 28))

        x_text = ''.join([t for _, t, _ in self.reader.readtext(np.array(current_x_screen))]).replace(" ", "")
        y_text = ''.join([t for _, t, _ in self.reader.readtext(np.array(current_y_screen))]).replace(" ", "")

        try:
            x_value = float(x_text)
            y_value = float(y_text)
        except ValueError:
            print("Не удалось распознать координаты")
            return None, None

        print(x_value, y_value)
        return x_value, y_value