from threading import Thread
from mrmine_keypress_detector import detect_keypress_nonblocking
from mrmine_gui import update_GUI, scroll, update_GUI_func
import os, time

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

def read_save():
	save_data = {}
	with open('mrmine_save.txt', 'r') as file:
		for line in file:
			line = line.strip()
			if '=' in line:  # Ensuring there's a key-value split
				key, value = line.split('=', 1)  # Split on first '=' to handle complex values
				try:
					# Attempt to evaluate the value for correct data types
					save_data[key] = eval(value)
				except Exception:
								# If eval fails, it's likely a string or ambiguous format
					save_data[key] = value
	return save_data

def mrmine_start_game():
	os.system('clear')
	try:
		save_data=read_save()
	except Exception:
		print("Error while loading save file.")
		save_data=None
		print("Exiting the game...")
		exit()
	if save_data['BROADCAST_TYPE'] != "none":
		print("Message from devs: "+save_data['BROADCAST_MESSAGE'])
		time.sleep(1)
		os.system('clear')
	try:
		listener_thread = Thread(target=keypress_listener)
		listener_thread.daemon = True
		listener_thread.start()
		update_GUI()
		while True:
			tick()
	except KeyboardInterrupt:
		print("Game interrupted, exiting...")
		exit()
