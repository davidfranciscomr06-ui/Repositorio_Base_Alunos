import pyautogui

pyautogui.PAUSE=1

# pyautogui.press()
pyautogui.hotkey('win','r')

pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.write("https://www.youtube.com/watch?v=6Jb8v7Zl6J4")
pyautogui.press("enter")

pyautogui.countdown(3)

pyautogui.click(1143,404)
pyautogui.write("")
pyautogui.press("enter")

pyautogui.click(1149,456)
pyautogui.write("")
pyautogui.press("enter")

# def aperta_tab(qtd):
#     for _ in range (qtd):
#         pyautogui.press('tab')
# aperta_tab(2)

#pyautogui.mouseInfo()