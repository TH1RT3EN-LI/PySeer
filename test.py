# import sys
# import os
# import sqlite3

# def creat_new_file(filename):
#     abspath = sys.path[0]
#     if os.path.exists(abspath + '\\default_files\\') is False:
#         os.makedirs(abspath + '\\default_files\\')
#     else:
#         all = os.listdir(abspath + '\\default_files\\')
#         if (filename + '.db') in all:
#             return False
#         else:
#             dbpath = abspath + '\\default_files\\' + filename + '.db'
#             conn = sqlite3.connect(dbpath)

#             c = conn.cursor()
#             c.execute("""CREATE TABLE PYSEER
#                 (ID  INT  PRIMARY KEY    NOT NULL, 
#                  PATH            TEXT    NOT NULL,
#                  MODE            INT     NOT NULL,
#                  LOOPID          INT     NOT NULL,
#                  LOOPTIMES       INT     NOT NULL);""")
#             conn.commit()
#             conn.close()
#             return dbpath
        

# def insert_into_file(dbpath, pngpath, id, mode, loopid=0, looptimes=0):
#     conn = sqlite3.connect(dbpath)
#     c = conn.cursor()
#     # if mode == 0:
#     #     c.execute("INSER INTO PYSEER (ID, PATH, MODE) \
#     #         VALUES (" + id + pngpath + mode +")")
#     # if mode == 1:
#     c.execute("INSER INTO PYSEER (ID, PATH, MODE, LOOPID, LOOPTIMES) \
#         VALUES (" + id + pngpath + mode + loopid + looptimes +")")
#     conn.commit()
#     conn.close()



# creat_new_file('学习力')
import sys
import cv2
import os
import sqlite3
import win32gui
from PIL import ImageQt, Image
import PyQt5.QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication

def select_target(id):
    image=cv2.imread(r'F:\PYTHON\PySeer\target_test\ad enter.png')

    r = cv2.selectROI('roi', image, True, False)
    # print(r)
    img_roi = image[int(r[1]):int(r[1]+r[3]),int(r[0]):int(r[0]+r[2])]
    # print(img_roi) 
    cv2.imshow("imageHSV",img_roi)
    img_pil = Image.fromarray(cv2.cvtColor(img_roi, cv2.COLOR_BGR2RGB))
    abspath = sys.path[0]
    if not os.path.exists(abspath + '\\target\\'):
        os.makedirs(abspath + '\\target\\')
    else:
        img_pil.save(abspath + '\\target\\' + str(id) + '.png')
    cv2.waitKey(0)
    return (abspath + '\\target\\' + str(id) + '.png')

select_target(11)