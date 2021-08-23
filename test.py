import pyautogui

while True:
    x , y = pyautogui.position()
    print(f"当前鼠标x轴位置{x}，当前鼠标y轴位置{y}")