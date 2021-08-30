import win32api, win32gui, win32con

hwnd = win32gui.FindWindow(0, 'ROI')

win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, 0x63, 0)
win32api.PostMessage(hwnd, win32con.WM_KEYUP, 0x63, 0)