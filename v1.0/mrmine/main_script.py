from threading import Thread
from mrmine_keypress_detector import detect_keypress_nonblocking
from mrmine_gui import update_GUI, scroll, update_GUI_func
import os

# Make the relay of keys more accessible
key_pressed = None

def keypress_listener():
	global key_pressed
	while True:
		key = detect_keypress_nonblocking()
		if key:
			key_pressed = key.lower()
			if key_pressed == '\x03':  # Ctrl+C for interrupt
				raise KeyboardInterrupt

def tick():
	global key_pressed
	while True:
		if key_pressed:
			key = key_pressed
			key_pressed = None
			print(f"Key registered: {key}")
			if key == 'up' or key == 'down':
				scroll(key)
				update_GUI()
			elif key in ["k", "q", "c", "s", "h", "u", " ", "p", "r"]:
				update_GUI_func(key)

def mrmine_start_game():
	os.system('clear')
	update_GUI()
	try:
		

	try:
		listener_thread = Thread(target=keypress_listener)
		listener_thread.daemon = True
		listener_thread.start()

		while True:
			tick()

	except KeyboardInterrupt:
		print("Game interrupted, exiting...")
