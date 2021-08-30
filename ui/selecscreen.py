import sys
import cv2
from PIL import Image
import Ui_create_new_file_4
import PyQt5.QtWidgets
import pyautogui
import win32api, win32gui, win32con

# im = pyautogui.screenshot(region=(0,0, 300, 400))
# while True:
#     if
#     x , y = pyautogui.position()
#     print(x, y)
# while True:
#     cv2.setMouseCallback(windowName, callbackFunc)
#     if cv2.setMouseCallback('13671188795', cv2.EVENT_MOUSEMOVE):
#         print('11')
# image=cv2.imread(r"F:\PYTHON\88888888.png")
# # cv2.namedWindow('img')
# r = cv2.selectROI('roi', image, True, False)
# print(r)
# img_roi = image[int(r[1]):int(r[1]+r[3]),int(r[0]):int(r[0]+r[2])]
# print(img_roi) 
# cv2.imshow("imageHSV",img_roi)
# img_pil = Image.fromarray(cv2.cvtColor(img_roi, cv2.COLOR_BGR2RGB))
# img_pil.save('xxghjx.png')
# cv2.waitKey(0)
class c4(PyQt5.QtWidgets.QDialog, Ui_create_new_file_4.Ui_CreateNewFile):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('TH1RT3EN PySeer')

    def bc(self):
        hwnd = win32gui.FindWindow(0, 'ROI')

        win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_SPACE, 0)
        win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_SPACE, 0)
        win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_SPACE, 0)
        win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_SPACE, 0) 
    

if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)

    mwin = c4()
    # # cnfa = CreateNewFileA()
    # cnfb = CreateNewFileB()
    # cnfc = CreateNewFileC()



    mwin.show()

    # mwin.pushButton.clicked.connect(cnfa.show)

    # cnfa.pushButton.clicked.connect(cnfb.show)

    # cnfb.pushButton_2.clicked.connect(cnfc.show)
    image=cv2.imread(r"F:\PYTHON\88888888.png")
    # cv2.namedWindow('img')
    r = cv2.selectROI('ROI', image, True, False)
    print(r)
    img_roi = image[int(r[1]):int(r[1]+r[3]),int(r[0]):int(r[0]+r[2])]
    print(img_roi) 

    img_pil = Image.fromarray(cv2.cvtColor(img_roi, cv2.COLOR_BGR2RGB))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    sys.exit(app.exec_())
    