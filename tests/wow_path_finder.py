import pyautogui
import time

imageX = pyautogui.screenshot(region=(918,4, 85, 25))
imageY = pyautogui.screenshot(region=(918,35, 85, 28))

x_file_name = "X_screenshot.png"
y_file_name = "Y_screenshot.png"

path_save = "D:/"

imageX.save(path_save+x_file_name)
imageY.save(path_save+y_file_name)