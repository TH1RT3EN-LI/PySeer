from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QImage
from PIL import ImageQt
import win32gui
import sys
import numpy as np
import cv2
import pyautogui
import random
from settings import Settings


def grab_window(windowname):
    """截图窗口可以被遮挡 操作要置顶 不能最小化"""
    hwnd = win32gui.FindWindow(0, windowname)
    # win32gui.SetForegroundWindow(hwnd)
    app = QApplication(sys.argv)
    screen = QApplication.primaryScreen()
    qimage = screen.grabWindow(hwnd).toImage()
    # 把QImage转换成Image
    image = ImageQt.fromqimage(qimage)
    return image


def matching_target(icon, image):
    """匹配图片 返回相对坐标"""
    screen = np.array(image)
    interface = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
    # target路径不能有中文
    target = cv2.imread(icon)
    methods = cv2.TM_SQDIFF_NORMED
    target_height, target_width = target.shape[:2]
    result = cv2.matchTemplate(interface, target, methods)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    # topleft/ bottomright
    tl = min_loc
    br = (tl[0] + target_width, tl[1] + target_height)
    return tl, br, min_val
    # # cv_imshow(interface, tl, br)
    # # if min_val != 0 and click_times > 0:
    # #     click_times = 0

    # #     location += 1
    # if min_val == 0:
    #     print(f' 目标相对左上坐标为{tl}, 相对右下坐标为{br}')
    #     random_click(tl, br, windowname, click_times, location)
    


def cv_imshow(interface, topleft, bottomright):
    """用cv2.imshow显示匹配情况"""
    cv2.rectangle(interface, topleft, bottomright, [0, 255, 0])
    cv2.imshow("open cv", interface)


def random_click(topleft, bottomright, windowname):
    """计算并随机点击绝对坐标范围内的某个点"""
    tl = topleft
    br = bottomright
    wx, wy = get_window_coordinate(windowname)
    x = random.randrange(tl[0], br[0])
    y = random.randrange(tl[1], br[1])
    pyautogui.click(x + wx, y + wy)


def get_window_coordinate(windowname):
    """得到窗口左上角坐标"""
    hwnd = win32gui.FindWindow(0, windowname)
    rect = win32gui.GetWindowRect(hwnd)
    x = rect[0]
    y = rect[1]
    return x, y


def run():
    """开始"""
    settings = Settings()
    icon = r'F:\PYTHON\PySeer\target\spacestation.png'
    while True:
        image = grab_window(settings.window_name)
        print(settings.location)
        icon = 'F:/PYTHON/PySeer/target' + '/' + str(settings.location) + '/target.png'
        tl, br, min_val = matching_target(icon, image)
        if min_val == 0:
            random_click(tl, br, settings.window_name)
            settings.click_times += 1
        if min_val != 0 and settings.click_times != 0:
            settings.click_times = 0
            settings.location += 1
        # if cv2.waitKey(25) & 0xFF == ord('q'):
        #     cv2.destroyAllWindows()
        #     break


if __name__ == "__main__":
    run()