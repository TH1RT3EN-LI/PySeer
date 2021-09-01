# 自带库
import os
import random
import sqlite3
import sys
# 第三方库
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
# 窗口UI
import ui.Ui_create_new_file_1
import ui.Ui_create_new_file_2
import ui.Ui_create_new_file_3
import ui.Ui_create_new_file_4
import ui.Ui_load_file_1
import ui.Ui_mainwindow


class MainWindow(PyQt5.QtWidgets.QMainWindow, ui.Ui_mainwindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('TH1RT3EN PySeer')
        self.setWindowlocation()

    def setWindowlocation(self):
        '''设置窗口位置于屏幕右上角'''
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(int(screen.width() - size.width()), 60)

    def btn_clicked(self):
        '''反馈新建按钮'''
        self.cnfa = CreateNewFileA()
        self.cnfa.show()

    def btn_clicked_2(self):
        '''反馈加载按钮'''
        self.lfa = LoadFileA()
        self.lfa.show()


class CreateNewFileA(PyQt5.QtWidgets.QWidget, ui.Ui_create_new_file_1.Ui_CreateNewFile):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('TH1RT3EN PySeer')
        self.text = 'test'
        self.setWindowlocation()

    def setWindowlocation(self):
        '''设置窗口位置于屏幕右上角'''
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(int(screen.width() - size.width()), 60)

    def update_text(self):
        '''实时更新脚本名'''
        self.text = self.lineEdit.text()

    def create_new_file(self):
        '''创建数据库存储脚本信息'''
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
                LOOPTIMES       INT     NOT NULL);""")
            conn.commit()
            conn.close()
        return dbpath

    def btn_clicked(self):
        '''反馈开始按钮'''
        self.cnfb = CreateNewFileB()
        self.cnfb.dbpath = self.create_new_file()
        self.cnfb.filename = self.text
        self.cnfb.show()
        self.close()
        

class CreateNewFileB(PyQt5.QtWidgets.QWidget, ui.Ui_create_new_file_2.Ui_CreateNewFile):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('TH1RT3EN PySeer')
        self.windowname = ''
        self.filename = ''
        self.looptimes = 2
        self.id = 1
        self.dbpath = ''
        self.pngpath = ''
        self.cnfd = CreateNewFileD()
        self.setWindowlocation()

    def setWindowlocation(self):
        '''设置窗口位置于屏幕右上角'''
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(int(screen.width() - size.width()), 60)

    def btn_clicked_1(self):
        '''添加目标'''
        self.mode = 0
        self.cnfd.show()
        self.pngpath = self.select_target(self.id, self.filename)
        if self.pngpath == 'NO':
            pass
        else:
            self.insert_into_file(self.dbpath, self.pngpath, self.id, self.mode)
            self.id += 1

    def btn_clicked_2(self):
        '''添加目标 循环开始'''
        self.cnfc = CreateNewFileC()
        self.cnfc._signal.connect(self.set_looptimes)
        self.mode = 1
        self.cnfd.show()
        self.cnfc.show()
        self.pngpath = self.select_target(self.id, self.filename)
        if self.pngpath == 'NO':
            pass
        else:
            # self.cnfc.setWindowModality(QtCore.Qt.ApplicationModal)
            self.insert_into_file(self.dbpath, self.pngpath, self.id, self.mode,
                                  self.looptimes)
            self.id += 1
    
    def btn_clicked_3(self):
        '''添加目标 循环结束'''
        self.mode = 2
        self.cnfd.show()
        self.pngpath = self.select_target(self.id, self.filename)
        if self.pngpath == 'NO':
            pass
        else:
            self.insert_into_file(self.dbpath, self.pngpath, self.id, self.mode,
                                  self.looptimes)
            self.id += 1

    def btn_clicked_4(self):
        '''完成'''
        self.looptimes = 2
        self.id = 1
        os.remove(r'PySeer\cache.png')
        self.close()

    def set_looptimes(self, loop):
        '''设置循环次数'''
        self.looptimes = loop
    
    def get_windowname(self):
        '''获取目标窗口名'''
        self.windowname = self.lineEdit.text()
    
    def insert_into_file(self, dbpath, pngpath, id, mode, looptimes=0):
        print(self.looptimes)
        conn = sqlite3.connect(dbpath)
        c = conn.cursor()
        c.execute(f"INSERT INTO PYSEER (ID, PATH, MODE, LOOPTIMES) \
            VALUES ({id}, '{pngpath}', {mode}, {looptimes})")
        conn.commit()
        conn.close()

    def grab_window(self):
        """截图"""
        hwnd = win32gui.FindWindow(0, self.windowname)
        screen = QApplication.primaryScreen()
        qimage = screen.grabWindow(hwnd).toImage()
        # 把QImage转换成Image
        image = ImageQt.fromqimage(qimage)
        image.save(r'PySeer\cache.png')

    def select_target(self, id, filename):
        '''用selectROI选择目标并保存'''
        image = cv2.imread(r'PySeer\cache.png')
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


class CreateNewFileC(PyQt5.QtWidgets.QDialog, ui.Ui_create_new_file_3.Ui_CreateNewFile):
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
        '''向上一个窗口传递输入的字符串'''
        self._signal.emit(int(self.lineEdit.text()))
        self.close()


class CreateNewFileD(PyQt5.QtWidgets.QDialog, ui.Ui_create_new_file_4.Ui_CreateNewFile):
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
        '''两次点击空格 保存roi选择区域'''
        self.hwnd = win32gui.FindWindow(0, 'ROI')
        win32api.PostMessage(self.hwnd, win32con.WM_KEYDOWN, win32con.VK_SPACE, 0)
        win32api.PostMessage(self.hwnd, win32con.WM_KEYUP, win32con.VK_SPACE, 0)
        win32api.PostMessage(self.hwnd, win32con.WM_KEYDOWN, win32con.VK_SPACE, 0)
        win32api.PostMessage(self.hwnd, win32con.WM_KEYUP, win32con.VK_SPACE, 0) 
        self.close()

    def btn_clicked_2(self):
        '''两次点击c 取消本次roi选择'''
        self.hwnd = win32gui.FindWindow(0, 'ROI')
        win32api.PostMessage(self.hwnd, win32con.WM_KEYDOWN, 0x43, 0)
        win32api.PostMessage(self.hwnd, win32con.WM_KEYUP, 0x43, 0)
        win32api.PostMessage(self.hwnd, win32con.WM_KEYDOWN, 0x43, 0)
        win32api.PostMessage(self.hwnd, win32con.WM_KEYUP, 0x43, 0)
        self.close()


class LoadFileA(PyQt5.QtWidgets.QWidget, ui.Ui_load_file_1.Ui_LoadFile):
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
        '''获取输入的数据库文件路径'''
        self.dbpath = self.lineEdit.text()

    def update_windowname(self):
        '''获取输入的窗口名'''
        self.windowname = self.lineEdit_2.text()

    def save_to_dict(self):
        '''读取数据库表格并存储于字典'''
        conn = sqlite3.connect(self.dbpath)
        c = conn.cursor()
        cursor = c.execute("SELECT ID, PATH, MODE, LOOPTIMES from PYSEER")
        for row in cursor:
            self.id_dict[row[0]] = [row[1], row[2], row[3]]
        conn.close()

    def random_click(self, topleft, bottomright):
        """计算并随机点击绝对坐标范围内的某个点"""
        tl = topleft
        br = bottomright
        x1, y1, x2, y2= self.get_window_coordinate()
        x = random.randrange(tl[0], br[0])
        y = random.randrange(tl[1], br[1])
        pyautogui.click(x + x1, y + y1)

    def get_window_coordinate(self):
        """得到窗口左上角坐标"""
        hwnd = win32gui.FindWindow(0, self.windowname)
        rect = win32gui.GetWindowRect(hwnd)
        x1 = rect[0]
        y1 = rect[1]
        x2 = rect[2]
        y2 = rect[3]
        return x1, y1, x2, y2

    def grab_window(self):
        """截图"""
        hwnd = win32gui.FindWindow(0, self.windowname)
        # win32gui.SetForegroundWindow(hwnd)
        screen = QApplication.primaryScreen()
        qimage = screen.grabWindow(hwnd).toImage()
        # 把QImage转换成Image
        image = ImageQt.fromqimage(qimage)
        return image

    def matching_target(self, icon, image):
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
    
    def prevent_sleep(self):
        '''防止休眠'''
        x1, y1, x2, y2 = self.get_window_coordinate()
        pyautogui.click((x2 - x1) / 2, y1 + 50)

    def btn_clicked_1(self):
        '''开始加载文件，匹配目标并点击'''
        self.save_to_dict()
        self.id = 1
        self.click_times = 0
        self.max_id = len(self.id_dict)
        self.loopstart = 0
        self.current_looptimes = 0

        while True:
            self.image = self.grab_window()
            self.mode = self.id_dict[self.id][1]
            self.path = self.id_dict[self.id][0]
            self.looptimes = self.id_dict[self.id][2]

            tl, br, min_val = self.matching_target(self.path, self.image)

            if min_val == 0:
                self.random_click(tl, br)
                self.click_times += 1
            if min_val != 0 and self.click_times != 0:
                self.click_times = 0

                if self.mode == 0:
                    self.id += 1
                if self.mode == 1:
                    self.loopstart = self.id
                    self.id += 1
                if self.mode == 2 and self.current_looptimes < self.looptimes:
                    self.current_looptimes += 1
                    self.id = self.loopstart
                if self.mode == 2 and self.current_looptimes == self.looptimes:
                    self.id += 1
                    self.current_looptimes = 0
            if min_val != 0 and self.click_times == 0:
                self.prevent_sleep(self)
            if self.id > self.max_id:
                break


if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    mwin = MainWindow()
    mwin.show()
    sys.exit(app.exec_())
