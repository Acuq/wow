import time
import win32api, win32con
import pyautogui

class MouseMover:
    def mouse_move_culc(self, direction, degrees):
        if direction != degrees:
            try:
                # Используем бинарный поиск для плавного поворота
                low, high = -360, 360
                while abs(high - low) > 0.1:  # Порог точности
                    mid = (low + high) / 2
                    turn = mid - direction
                    #if turn > 180:
                        #print(f"Превышение максимального угла поворота: {turn}")
                        #return
                    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 960, 540, 0, 0)
                    time.sleep(0.03)
                    pyautogui.moveTo(960 + turn, 540)
                    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 960, 540, 0, 0)
                    print(mid, "- угол ", direction, "- направление ")

                    if mid < degrees:
                        low = mid
                    else:
                        high = mid

                # Финальный поворот
                final_turn = degrees - direction
                #if final_turn > 180:
                    #print(f"Превышение максимального угла поворота: {final_turn}")
                    #return
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 960, 540, 0, 0)
                time.sleep(0.03)
                pyautogui.moveTo(960 + final_turn, 540)
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 960, 540, 0, 0)
                print(degrees, "- угол ", direction, "- направление ")

            except Exception as e:
                print(f"Ошибка при коррекции направления мыши: {e}")