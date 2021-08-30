import pyautogui
import cv2
from PIL import Image

# im = pyautogui.screenshot(region=(0,0, 300, 400))
# while True:
#     if
#     x , y = pyautogui.position()
#     print(x, y)
# while True:
#     cv2.setMouseCallback(windowName, callbackFunc)
#     if cv2.setMouseCallback('13671188795', cv2.EVENT_MOUSEMOVE):
#         print('11')
image=cv2.imread(r'F:\PYTHON\PySeer\target\ad enter.png')
# cv2.namedWindow('img')
r = cv2.selectROI('roi', image, True, False)
print(r)
img_roi = image[int(r[1]):int(r[1]+r[3]),int(r[0]):int(r[0]+r[2])]
print(img_roi) 
cv2.imshow("imageHSV",img_roi)
img_pil = Image.fromarray(cv2.cvtColor(img_roi, cv2.COLOR_BGR2RGB))
img_pil.save('xxghjx.png')
cv2.waitKey(0)

