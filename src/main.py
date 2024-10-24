from AutoMove import *



def main():
    
    x_point, y_point = path.path_reader('route')
    direction = direction_calculate.calculate_azimuth(0,x_point, y_point)
    print(direction, 'direction')

    while True:
        win32api.keybd_event(0x57, 0, 0, 0)  # Key down
        zone = direction_calculate.calculate_azimuth(0,x_point, y_point)
        print(zone)
        direction_calculate.dirrect_corretion_mouse_move(direction,degrees=direction_calculate.calculate_azimuth(0,x_point, y_point))
        direction_calculate.dirrect_coordinate_position(0,x_point,y_point)

        if keyboard.is_pressed('esc'):
            print("Script stopped.")
            win32api.keybd_event(0x57, 0, win32con.KEYEVENTF_KEYUP, 0)  # Key up
            break
        




main()