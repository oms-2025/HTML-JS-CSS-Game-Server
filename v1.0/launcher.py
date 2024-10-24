import time, os, random
from mrmine_main import mrmine_start_game
from colorama import Fore as color

print("""
Enter the ID for the game you would like to play.
1. Mr. Mine [WIP]""")
game=input(" > ")
try:
	game=int(game)
except Exception:
	print("Invalid ID.")
	exit()
if game==1:
	print("Starting Mr. Mine...")
	time.sleep(0.5)
	print("Loading Game...")
	time.sleep(random.uniform(0.5, 1.5))
	os.system('clear')
	i=0
	d1=random.randint(-3, 3)
	d2=random.randint(-3, 3)
	d3=random.randint(-3, 3)
	while i<=100:
		print("="*102)
		print("|"+color.GREEN+"█"*i+color.WHITE+"█"*(100-i)+"|")
		print("|"+color.GREEN+"█"*i+color.WHITE+"█"*(100-i)+"|")
		print("|"+color.GREEN+"█"*i+color.WHITE+"█"*(100-i)+"|","("+str(i)+"%)")
		print("="*102)
		if i<=15+d1:
			print(color.WHITE+"Loading Launcher...")
		elif i<=50+d2:
			print(color.WHITE+"Initializing Game...")
		elif i<=80+d3:
			print(color.WHITE+"Loading GUI...")
		elif i<100:
			print("Loading Scripts...")
		elif i==100:
			break
		time.sleep(random.uniform(0.1, 0.3))
		os.system('clear')
		i+=1
	print(color.WHITE+"Loading Complete!")
	time.sleep(2)
	print(color.WHITE+"Welcome to Mr. Mine!")
	time.sleep(1)
	os.system('clear')
	mrmine_start_game()
