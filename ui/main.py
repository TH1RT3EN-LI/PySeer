import os
import random
import sqlite3
import sys

import cv2
import numpy as np
import pyautogui
import PyQt5.QtWidgets
import win32api
import win32con
import win32gui
from PIL import Image, ImageQt
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QDesktopWidget

import Ui_create_new_file_1
import Ui_create_new_file_2
import Ui_create_new_file_3
import Ui_create_new_file_4
import Ui_load_file_1
import Ui_mainwindow


class MainWindow(PyQt5.QtWidgets.QMainWindow, Ui_mainwindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('TH1RT3EN PySeer')
        self.setWindowlocation()

    def setWindowlocation(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(int(screen.width() - size.width()), 60)

    def btn_clicked(self):
        self.cnfa = CreateNewFileA()
        self.cnfa.show()

    def btn_clicked_2(self):
        self.lfa = LoadFileA()
        self.lfa.show()


class CreateNewFileA(PyQt5.QtWidgets.QWidget, Ui_create_new_file_1.Ui_CreateNewFile):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('TH1RT3EN PySeer')
        self.text = 'test'
        self.setWindowlocation()

    def setWindowlocation(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(int(screen.width() - size.width()), 60)

    def update_text(self):
        self.text = self.lineEdit.text()

    def create_new_file(self):
        abspath = sys.path[0]
        if os.path.exists(abspath + '\\default_files\\') is False:
            os.makedirs(abspath + '\\default_files\\')
        else:
            pass
        all = os.listdir(abspath + '\\default_files\\')

        if (self.text + '.db') in all:
            return False
        else:
            dbpath = abspath + '\\default_files\\' + self.text + '.db'
            conn = sqlite3.connect(dbpath)
            c = conn.cursor()
            c.execute("""CREATE TABLE PYSEER
                (ID  INT  PRIMARY KEY   NOT NULL, 
                PATH            TEXT    NOT NULL,
                MODE            INT     NOT NULL,
                LOOPID          INT     NOT NULL,
                LOOPTIMES       INT     NOT NULL);""")
            conn.commit()
            conn.close()
        return dbpath

    def btn_clicked(self):
        self.cnfb = CreateNewFileB()
        self.cnfb.dbpath = self.create_new_file()
        self.cnfb.filename = self.text
        self.cnfb.show()
        

class CreateNewFileB(PyQt5.QtWidgets.QWidget, Ui_create_new_file_2.Ui_CreateNewFile):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('TH1RT3EN PySeer')
        self.windowname = ''
        self.filename = ''
        self.looptimes = 2
        self.id = 1
        self.loopid = 1
        self.dbpath = ''
        self.pngpath = ''
        self.cnfd = CreateNewFileD()
        self.setWindowlocation()

    def setWindowlocation(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(int(screen.width() - size.width()), 60)

    def btn_clicked_1(self):
        self.mode = 0
        print(self.dbpath)
        self.cnfd.show()
        self.pngpath = self.select_target(self.id, self.filename)
        if self.pngpath == 'NO':
            print('NO')
            pass
        else:
            print(self.pngpath)
            self.insert_into_file(self.dbpath, self.pngpath, self.id, self.mode)
            self.id += 1

    def btn_clicked_2(self):
        self.cnfc = CreateNewFileC()
        self.cnfc._signal.connect(self.set_looptimes)
        self.mode = 1
        self.cnfd.show()
        self.pngpath = self.select_target(self.id, self.filename)
        if self.pngpath == 'NO':
            print('NO')
            pass
        else:
            print(self.pngpath)
            self.cnfc.show()
            self.insert_into_file(self.dbpath, self.pngpath, self.id, self.mode,
                                  self.loopid, self.looptimes)
            self.id += 1

    def btn_clicked_3(self):
        self.mode = 0
        self.cnfd.show()
        self.pngpath = self.select_target(self.id, self.filename)
        if self.pngpath == 'NO':
            print('NO')
            pass
        else:
            print(self.pngpath)
            self.insert_into_file(self.dbpath, self.pngpath, self.id, self.mode)
            self.id += 1

    
    def btn_clicked_4(self):
        self.mode = 2
        self.cnfd.show()
        self.pngpath = self.select_target(self.id, self.filename)
        if self.pngpath == 'NO':
            print('NO')
            pass
        else:
            print(self.pngpath)
            self.insert_into_file(self.dbpath, self.pngpath, self.id, self.mode)
            self.id += 1
            self.loopid += 1

    def btn_clicked_5(self):
        self.looptimes = 2
        self.id = 1
        self.loopid = 1
        os.remove('F:\PYTHON\PySeer\cache.png')
        self.close()

    def set_looptimes(self, loop):
        self.looptimes = loop
    
    def get_windowname(self):
        self.windowname = self.lineEdit.text()
    
    def insert_into_file(self, dbpath, pngpath, id, mode, loopid=0, looptimes=0):
        conn = sqlite3.connect(dbpath)
        c = conn.cursor()
        c.execute(f"INSERT INTO PYSEER (ID, PATH, MODE, LOOPID, LOOPTIMES) \
            VALUES ({id}, '{pngpath}', {mode}, {loopid}, {looptimes})")
        conn.commit()
        conn.close()

    def grab_window(self):
        """截图窗口可以被遮挡 操作要置顶 不能最小化"""
        hwnd = win32gui.FindWindow(0, self.windowname)
        screen = QApplication.primaryScreen()
        qimage = screen.grabWindow(hwnd).toImage()
        # 把QImage转换成Image
        image = ImageQt.fromqimage(qimage)
        print(self.windowname, image)
        image.save(r'F:\PYTHON\PySeer\cache.png')

    def select_target(self, id, filename):
        image = cv2.imread(r'F:\PYTHON\PySeer\cache.png')
        r = cv2.selectROI('ROI', image, True, False)
        if r == (0, 0, 0, 0):
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            return 'NO'
        else:
            x, y, w, h = r
            img_roi = image[y:y+h, x:x+w]
            img_pil = Image.fromarray(cv2.cvtColor(img_roi, cv2.COLOR_BGR2RGB))
            abspath = sys.path[0]
            if not os.path.exists(abspath + '\\target\\' + filename + '\\'):
                os.makedirs(abspath + '\\target\\' + filename + '\\')
            img_pil.save(abspath + '\\target\\' + filename + '\\' + str(id) + '.png')
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            return (abspath + '\\target\\' + filename + '\\' + str(id) + '.png')


class CreateNewFileC(PyQt5.QtWidgets.QDialog, Ui_create_new_file_3.Ui_CreateNewFile):
    _signal = QtCore.pyqtSignal(int)
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('TH1RT3EN PySeer')
        self.setWindowlocation()

    def setWindowlocation(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(int(screen.width() - size.width()), 60)

    def get_loop_times(self):
        self._signal.emit(int(self.lineEdit.text()))
        self.close()


class CreateNewFileD(PyQt5.QtWidgets.QDialog, Ui_create_new_file_4.Ui_CreateNewFile):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('TH1RT3EN PySeer')
        self.setWindowlocation()

    def setWindowlocation(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(int(screen.width() - size.width()), 60)
    
    def btn_clicked_1(self):
        self.hwnd = win32gui.FindWindow(0, 'ROI')
        win32api.PostMessage(self.hwnd, win32con.WM_KEYDOWN, win32con.VK_SPACE, 0)
        win32api.PostMessage(self.hwnd, win32con.WM_KEYUP, win32con.VK_SPACE, 0)
        win32api.PostMessage(self.hwnd, win32con.WM_KEYDOWN, win32con.VK_SPACE, 0)
        win32api.PostMessage(self.hwnd, win32con.WM_KEYUP, win32con.VK_SPACE, 0) 
        self.close()

    def btn_clicked_2(self):
        self.hwnd = win32gui.FindWindow(0, 'ROI')
        win32api.PostMessage(self.hwnd, win32con.WM_KEYDOWN, 0x43, 0)
        win32api.PostMessage(self.hwnd, win32con.WM_KEYUP, 0x43, 0)
        win32api.PostMessage(self.hwnd, win32con.WM_KEYDOWN, 0x43, 0)
        win32api.PostMessage(self.hwnd, win32con.WM_KEYUP, 0x43, 0)
        self.close()


class LoadFileA(PyQt5.QtWidgets.QWidget, Ui_load_file_1.Ui_LoadFile):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('TH1RT3EN PySeer')
        self.dbpath = ''
        self.id_dict = {}
        self.windowname = ''
        self.setWindowlocation()

    def setWindowlocation(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(int(screen.width() - size.width()), 60)

    def update_dbpath(self):
        self.dbpath = self.lineEdit.text()

    def update_windowname(self):
        self.windowname = self.lineEdit.text()

    def save_to_dict(self):
        conn = sqlite3.connect(self.dbpath)
        c = conn.cursor()
        cursor = c.execute("SELECT ID, PATH, MODE, LOOPID, LOOPTIMES from PYSEER")
        for row in cursor:
            self.id_dict[row[0]] = [row[1], row[2], row[3], row[4]]
        conn.close()

    def random_click(self, topleft, bottomright, windowname):
        """计算并随机点击绝对坐标范围内的某个点"""
        tl = topleft
        br = bottomright
        wx, wy = self.get_window_coordinate(windowname)
        x = random.randrange(tl[0], br[0])
        y = random.randrange(tl[1], br[1])
        pyautogui.click(x + wx, y + wy)

    def get_window_coordinate(self, windowname):
        """得到窗口左上角坐标"""
        hwnd = win32gui.FindWindow(0, windowname)
        rect = win32gui.GetWindowRect(hwnd)
        x = rect[0]
        y = rect[1]
        return x, y

    def grab_window(self, windowname):
        """截图窗口可以被遮挡 操作要置顶 不能最小化"""
        print(99)
        hwnd = win32gui.FindWindow(0, windowname)
        # win32gui.SetForegroundWindow(hwnd)
        screen = QApplication.primaryScreen()
        qimage = screen.grabWindow(hwnd).toImage()
        # 把QImage转换成Image
        image = ImageQt.fromqimage(qimage)

        return image

    def matching_target(self, icon, image):
        """匹配图片 返回相对坐标"""
        print('matching')
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


    def btn_clicked_1(self):
        self.save_to_dict()
        self.id = 1
        self.click_success = 1
        self.click_times = 0
        self.max_id = len(self.id_dict)
        print(1)
        while True:
            print(2)
            self.image = self.grab_window(self.windowname)
            if self.click_success == 1:
                print(self.id_dict)
                
                self.mode = self.id_dict[self.id][1]
                self.path = self.id_dict[self.id][0]
                self.loopid = self.id_dict[self.id][2]
                self.looptimes = self.id_dict[self.id][3]
                self.loopstart = 0
                self.loopend = 0
                if self.mode == 0:
                    tl, br, min_val = self.matching_target(self.path, self.image)
                    id += 1
                if self.mode == 1:
                    tl, br, min_val = self.matching_target(self.path, self.image)
                    loopstart = self.id
                if self.mode == 2:
                    loopend = self.id
                    tl, br, min_val = self.matching_target(self.path, self.image)
                    if self.looptimes > 0:
                        self.looptimes -= 1
                        id = loopstart
                    if self.looptimes == 0:
                        id = loopend
            else:
                print(4)
                pass
            if min_val == 0:
                self.random_click(tl, br, self.windowname)
                self.click_times += 1
            if min_val != 0 and self.click_times != 0:
                self.click_times = 0
                self.click_success = 1
            if self.id > self.max_id:
                break
        print(5)
            

if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    mwin = MainWindow()
    mwin.show()
    sys.exit(app.exec_())
