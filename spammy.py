import pyautogui, time
print("\u001b[31mWARNING!!!")


time.sleep(1)

print("\u001b[31m")

print("\u001b[31mDO NOT ABUSE AND OR USE WITHOUT CONSENT OR FOR HARASSMENT")

2
time.sleep(2)

msg = input("\u001b[33mEnter Your message: ")
n = input("\u001b[33mHow many times would you like it to be spammed?: ")

print("\u001b[34mstarting in:")
print("\u001b[36m")
time.sleep(1)

count = 5
while(count != 0):
	print(count)
	time.sleep(1)
	count -= 1

print("\u001b[31mFire in the hole!!!")

time.sleep(1)

for i in range(0,int(n)):
   	pyautogui.typewrite(msg + '\n')


