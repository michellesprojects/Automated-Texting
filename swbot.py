import pyautogui

#move mouse to the x & y coordinates of where the message text box is
pyautogui.moveTo(83,799,1)

pyautogui.click()


file = open('swscript.txt','r')

for line in file:
	line = line.strip()
	if len(line) > 0:
		pyautogui.write(line)
		pyautogui.press('enter')

