import pyautogui
import easyocr
import numpy as np
import time
import keyboard
import os
import math
import win32api,win32con
reader = easyocr.Reader(['en'])


class Position:
    def current_char_position(self):
        try:
            current_x_screen = pyautogui.screenshot(region=(760,1, 200, 60))
            current_y_screen = pyautogui.screenshot(region=(950,1, 215, 60))

            x_value = float(''.join([t for _, t, _ in reader.readtext(np.array(current_x_screen))]).replace(" ", ""))
            y_value = float(''.join([t for _, t, _ in reader.readtext(np.array(current_y_screen))]).replace(" ", ""))

            return x_value, y_value
        except:
            print('не видно координаты')

class Path:
    def path_recorder(self):
        try:
            print("Кнопка - n отвечает за сохранение координаты. Кнопка - j отвечает за сохранение маршрута")
            x_coordinates = []
            y_coordinates = []
            while True:

                if keyboard.is_pressed('n'):
                    time.sleep(1)
                    x_value, y_value = position.current_char_position()
                    x_coordinates.append(x_value)
                    y_coordinates.append(y_value)
                    print("Координаты сохраненны ")

                if keyboard.is_pressed('j'):
                    time.sleep(1)
                    filename = input("Введите название маршрута - ")
                    script_dir = os.path.dirname(__file__)
                    routes_dir = os.path.join(script_dir, 'routes')
                    if not os.path.exists(routes_dir):
                        os.makedirs(routes_dir)
                    file_path = os.path.join(routes_dir, filename+'.txt')
                    with open(file_path, 'w') as f:
                        for i in range(len(x_coordinates)):
                            f.write(f"{x_coordinates[i]}, {y_coordinates[i]}\n")
                    print("Координаты сохраненны в папку routes")
                    break
        except:
            print('ошибка записи маршрута')


    def path_reader(self,filename):
        try:
            script_dir = os.path.dirname(__file__)
            routes_dir = os.path.join(script_dir, 'routes')
            file_path = os.path.join(routes_dir, filename+'.txt')
            x_coordinates = []
            y_coordinates = []
            with open(file_path, 'r') as f:
                for line in f:
                    x, y = line.strip().split(', ')
                    x_coordinates.append(float(x))
                    y_coordinates.append(float(y))
            return x_coordinates, y_coordinates
        except:
            print('ошибка чтении маршрута')
    
class DirectionCalculate:
    
    def calculate_azimuth(self,waypoint,x_point, y_point):
        try:
            x_current, y_current = position.current_char_position()
                
            dx = x_point[waypoint] - x_current
            dy = y_point[waypoint] - y_current

            radians = math.atan2(dy, dx)
            degrees = math.degrees(radians*2)


            return round(degrees, 3)
        except:
            print('ошибка азимута')

    def dirrect_corretion_mouse_move(self,direction,degrees):
        try:

            if degrees > direction:
                turn = degrees - direction
                print(turn, 'TURN RIGHT')
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 960, 540, 0, 0)
                time.sleep(0.03)
                pyautogui.moveTo(960+abs(turn), 540) #right
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 960, 540, 0, 0)

            elif degrees < direction:
                turn = degrees - direction
                print(turn, 'TURN LEFT')
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 960, 540, 0, 0)
                time.sleep(0.03)
                pyautogui.moveTo(960-abs(turn), 540) #left
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 960, 540, 0, 0)

        except:
            print('ошибка направлении мыши')

    def dirrect_coordinate_position(self,waypoint,x_point,y_point):
            x_current, y_current = position.current_char_position()
            x_start = x_point[waypoint] - x_current
            y_start = y_point[waypoint] - y_current
            x_current, y_current = position.current_char_position()
            x_step = x_point[waypoint] - x_current
            y_step = y_point[waypoint] - y_current
            print(y_start,y_step)
            if(y_start > y_step):
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 960, 540, 0, 0)
                time.sleep(0.03)
                pyautogui.moveTo(1700, 540)
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 960, 540, 0, 0)


        




########
position = Position()
direction_calculate = DirectionCalculate()
path = Path()
########
























