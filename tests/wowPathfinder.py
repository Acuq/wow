import pyautogui
import time

imageX = pyautogui.screenshot(region=(760,1, 200, 60))
imageY = pyautogui.screenshot(region=(950,1, 215, 60))

file_name = str(time.time()) + ".png"
imageX.save("D:/" + 'X'+file_name)

file_name = str(time.time()) + ".png"
imageY.save("D:/" + 'Y'+file_name)