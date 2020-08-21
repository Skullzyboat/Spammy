import pyautogui
import time

msg = input("Enter Your message: ")
n = input("How many times would you like it to be spammed? ?: ")

print("t minus")

count = 5
while(count != 0):
	print(count)
	time.sleep(1)
	count -= 1

print("\u001b[31mFire in the hole!!!")

for i in range(0,int(n)):
	pyautogui.typewrite(msg + '\n')
