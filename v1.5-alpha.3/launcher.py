import time, os, random
from mrmine.main_script import mrmine_start_game, m_ms_initialize
from mrmine.keypress_detector import m_kd_initialize
from mrmine.gui import m_g_initialize
from clicker.main_script import clicker_start_game
from mrmine_integrity import m_ic_initialize
os.system('clear')
m_version='v1.5-alpha.3'
print(f'''
You are on version {m_version}.
To see all versions go to:
https://github.com/XtheGxmerz0/coolmathgames''')
time.sleep(0.75)
print('''
Enter the ID for the game you would like to play.
1. Mr. Mine                            | [v1.5-alpha.3, Work-In-Progress]
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
	print('Initializing main script...')
	m_ms_initialize()
	print('Initializing GUI...')
	m_g_initialize()
	print('Initializing keypress detector...')
	m_kd_initialize()
	print('Performing integrity check...')
	m_ic_initialize()
	print("Loading Complete!")
	time.sleep(1)
	print("Welcome to Mr. Mine!")
	time.sleep(0.5)
	os.system('clear')
	mrmine_start_game()