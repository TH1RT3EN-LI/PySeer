from PIL.Image import Image
import numpy
from PIL import ImageGrab
import time
import win32gui
import cv2
import pyautogui
import random



class PySeer:

    def __init__(self,name):
        '''初始化窗口'''
        self.find_window = win32gui.FindWindow(0, name)
        self.point = (0, 0, 1440, 900)
        self.current_page = 0
        self.png = r'PySeer\target\map.png'
    
    # def setwindow(self):
        

    def getscreen(self):
        
        while True:

            game_interface = ImageGrab.grab(self.point)
            screen = numpy.array(game_interface)
            target = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
            # 路径不能有中文
            tpl = cv2.imread(self.png)
            methods = cv2.TM_SQDIFF_NORMED
            th, tw = tpl.shape[:2]
            result = cv2.matchTemplate(target, tpl, methods)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            tl = min_loc
            br = (tl[0] + tw, tl[1] + th)
            cv2.rectangle(target, tl, br, [0, 255, 0])
            cv2.imshow("open cv", target)
            if min_val == 0:
                print(f'tpl 左上坐标为{tl}, 右下坐标为{br}')
                xa, ya = tl
                xb, yb = br
                x = random.randrange(tl[1], xb)
                y = random.randrange(ya, yb)
                pyautogui.click(x, y)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break


        

if __name__ == "__main__":
    wname = '13671188795'

    demo = PySeer(wname)
    demo.setwindow()
    demo.getscreen()
