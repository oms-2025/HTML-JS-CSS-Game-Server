import time, os, random
from mrmine.main_script import mrmine_start_game
from clicker.main_script import clicker_start_game
from colorama import Fore as color
os.system('clear')
version='v1.3-alpha'
print(f'''
You are on version {version}.
To see all versions go to:
https://github.com/XtheGxmerz0/coolmathgames''')
time.sleep(0.75)
print('''
Enter the ID for the game you would like to play.
1. Mr. Mine                            | [v1.3-alpha, Work-In-Progress]
2: Clicker Game                        | [v1.0, Work-In-Progress]''')
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
	while i<100:
		os.system('clear')
		print("="*102)
		print("|"+color.GREEN+("█"*i)+color.WHITE+("█"*(100-i))+"|")
		print("|"+color.GREEN+("█"*i)+color.WHITE+("█"*(100-i))+"| ("+str(i)+"%)")
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
		i+=1
		time.sleep(random.uniform(0.05, 0.2))
	os.system('clear')
	print("="*102)
	print("|"+color.GREEN+("█"*100)+color.WHITE+"|")
	print("|"+color.GREEN+("█"*100)+color.WHITE+"| (100%)")
	print("="*102)
	print(color.WHITE+"Loading Complete!")
	time.sleep(1)
	print(color.WHITE+"Welcome to Mr. Mine!")
	time.sleep(0.5)
	os.system('clear')
	mrmine_start_game()
