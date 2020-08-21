import pyautogui
import time

msg = input("\u001b[33mEnter Your message: ")
n = input("\u001b[33mHow many times would you like it to be spammed? ?: ")

print("\u001b[34mstarting in:")

count = 5
while(count != 0):
	print(count)
	time.sleep(1)
	count -= 1

print("\u001b[31mFire in the hole!!!")

for i in range(0,int(n)):
	pyautogui.typewrite(msg + '\n')
