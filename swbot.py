import pyautogui

#move mouse to the x & y coordinates of where the text box is to type your message
pyautogui.moveTo(83,799,1)

pyautogui.click() #this code is optimized for the desktop discord application, this lines clicks onto the text box for messages

file = open('swscript.txt','r') #file with swscript

for line in file: #iterating through all lines in the script
	line = line.strip() 
	if len(line) > 0: #ignoring lines with 0 chars
		pyautogui.write(line) #write line into text box
		pyautogui.press('enter') #press enter to send messsage

