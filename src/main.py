import pyautogui
import easyocr
import numpy as np
import time
import keyboard
import os
import math
import win32api,win32con

reader = easyocr.Reader(['en'])

def current_char_position():
    current_x_screen = pyautogui.screenshot(region=(918,4, 85, 25))
    current_y_screen = pyautogui.screenshot(region=(918,35, 85, 28))

    x_value = float(''.join([t for _, t, _ in reader.readtext(np.array(current_x_screen))]).replace(" ", ""))
    y_value = float(''.join([t for _, t, _ in reader.readtext(np.array(current_y_screen))]).replace(" ", ""))

    #print(x_value,y_value,end='\r')
    print(y_value,y_value)

    return x_value,y_value


def path_recorder():
    print("Кнопка - n отвечает за сохранение координаты. Кнопка - j отвечает за сохранение маршрута")
    x_coordinates = []
    y_coordinates = []
    while True:

        if keyboard.is_pressed('n'):
            time.sleep(1)
            x_value, y_value = current_char_position()
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


def path_reader(filename):
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


def calculate_azimuth(waypoint,x_point, y_point):
    x_current, y_current = current_char_position()
    
    dx = x_point[waypoint] - x_current
    dy = y_point[waypoint] - y_current
    radians = math.atan2(dy, dx)
    degrees = math.degrees(radians*2)

    print(degrees)
    return degrees


def dirrect_corretion_mouse_move(direction,degrees):

    if degrees > direction:
        turn = degrees - direction
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 960, 540, 0, 0)
        time.sleep(0.03)
        pyautogui.moveTo(960+turn, 540)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 960, 540, 0, 0)
        print(degrees,"- угол ", direction,"- направление ПРАВО ")

    elif degrees < direction:
        turn = direction - degrees
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 960, 540, 0, 0)
        time.sleep(0.03)
        pyautogui.moveTo(960-turn, 540)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 960, 540, 0, 0)
        print(degrees,"- угол ", direction,"- направление ЛЕВО ")

while True:
    current_char_position()