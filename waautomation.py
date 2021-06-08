import pyautogui
import webbrowser
import time
for i in range(4):
      url="https://wa.me/919390409846?text=madhu"
      webbrowser.open(url)
      pos=(1000,418)
      pyautogui.moveTo(pos)
      time.sleep(3)
      pyautogui.press("enter")
      pyautogui.press("enter")
      time.sleep(3)
      pyautogui.press("enter")
      time.sleep(2)

"""
while(True):
      print(pyautogui.position())
"""
