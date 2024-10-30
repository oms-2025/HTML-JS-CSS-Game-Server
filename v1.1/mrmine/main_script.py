from threading import Thread
import threading
from mrmine.keypress_detector import detect_keypress_nonblocking
from mrmine.gui import update_GUI, scroll, update_GUI_func, GUI_send, get_save
import os, time, random, math
global save_data
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
			key_pressed = False
			print(f"Key registered: {key}")
			if key == 'up' or key == 'down':
				scroll(key)
				update_GUI()
			elif key in ["k", "q", "c", "s", "h", "u", " ", "p", "r"]:
				update_GUI_func(key)
		else:
			time.sleep(0.1)
			update_GUI()

def drill_percent():
	global save_data
	while True:
		drill_data=save_data['DRILL_DATA']
		time_to_new_depth=drill_data[0]/save_data['LAYER_HARDNESS']
		start_new_depth=time.time()
		end_new_depth=start_new_depth+time_to_new_depth
		while time.time()<=end_new_depth:
			percent=round(((time.time()-start_new_depth)/time_to_new_depth)*100, 2)
			GUI_send(percent, "percent_to_new_layer")
			time.sleep(0.5)
		save_data['DEPTH']+=1
		save_data['LAYER_HARDNESS']=float((1.57**(1+(save_data['DEPTH']/50)))-0.57)
		GUI_send('new_depth', 'signal')
def miner_monitor():
	global save_data
	while True:
		i=1
		resource_input={
		1: 0,
		2: 0,
		3: 0,
		4: 0,
		5: 0,
		6: 0,
		7: 0,
		8: 0,
		9: 0,
		10: 0,
		11: 0,
		12: 0,
		13: 0,
		14: 0,
		15: 0
		}
		while i<=save_data['DEPTH']:
			x100depth=math.ceil(i/100)
			#1-100km: 0.2 coal / sec, 0.07 copper / sec, 0.003 iron / sec
			#101-200km: 0.2 copper / sec, 0.07 iron / sec, 0.003 silver / sec
			#etc.
			if x100depth*100<=save_data['DEPTH']:
				resource_input[x100depth]+=(0.2)*save_data['MINER_SPEED']*save_data['MINER_EFFICIENCY']*100
				resource_input[x100depth+1]+=(0.07)*save_data['MINER_SPEED']*save_data['MINER_EFFICIENCY']*100
				resource_input[x100depth+2]+=(0.003)*save_data['MINER_SPEED']*save_data['MINER_EFFICIENCY']*100
			else:
				resource_input[x100depth]+=(0.2)*save_data['MINER_SPEED']*save_data['MINER_EFFICIENCY']*(save_data['DEPTH']-((x100depth-1)*100))
				resource_input[x100depth+1]+=(0.07)*save_data['MINER_SPEED']*save_data['MINER_EFFICIENCY']*(save_data['DEPTH']-((x100depth-1)*100))
				resource_input[x100depth+2]+=(0.003)*save_data['MINER_SPEED']*save_data['MINER_EFFICIENCY']*(save_data['DEPTH']-((x100depth-1)*100))
			i+=100
		for mineral in resource_input:
			save_data['MINERALS'][mineral-1]+=resource_input[mineral]
			save_data['MINERALS'][mineral-1]=int(round(save_data['MINERALS'][mineral-1], 0))
		time.sleep(0.1)
drill_thread=threading.Thread(target=drill_percent)
miner_thread=threading.Thread(target=miner_monitor)
def read_save():
	save_data = {
'SAVE_NUMBER': 1,
'END_TIME': 0,
'STORAGE': 0,
'UPGRADES': [],
'MINERALS': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
'FLUIDS': [0, 0, 0],
'SCIENTIST_DATA': [],
'CAVE_DATA': [],
'CHEST_DATA': [],
'MONEY': 0,
'TP_DATA': [],
'MANAGER': (0.00, 0),
'ATTACK': (0, 0),
'MINER_SPEED': 1,
'MINER_EFFICIENCY': 1,
'DEPTH': 10,
'DRILL_DATA': [],
'RIG_DATA': [],
'LAYER_HARDNESS': 1,
'FORGE_STATUS': 'none',
'BROADCAST': '',
'BROADCAST_TYPE': 'none',
'DATAID': 0,
'PLANET': 1
	}
	with open('/workspaces/coolmathgames/v1.0/mrmine/mrmine_save.txt', 'r') as file:
		for line in file:
			line = line.strip()
			if '=' in line:  # Ensuring there's a key-value split
				key, value = line.split('=', 1)  # Split on first '=' to handle complex values
				try:
					# Attempt to evaluate the value for correct data types
					save_data[key] = eval(value)
				except Exception:
					print("Error reading save file key")
					# If eval fails, it's likely a string or ambiguous format
					save_data[key] = value
	return save_data
def send_data_to_GUI():
	while True:
		get_save(save_data)
		time.sleep(0.02)
send_thread=threading.Thread(target=send_data_to_GUI)
def write_save(save_data):
	success=False
	i=1
	while i<=5 and not success:
		try:
			with open('/workspaces/coolmathgames/v1.0/mrmine/mrmine_save.txt', 'w') as file:
				print("opened save file")
				strv=''''''
				for item in save_data:
					print("writing item",item)
					strv += item + '=' + str(save_data[item]) + '\n'
				file.writelines(strv)
				print("success")
				success=True
				break
		except Exception:
			print(f"Error while saving the game. (Attempt {i}/5)")
			i+=1

def mrmine_start_game():
	global save_data
	os.system('clear')
	try:
		save_data=read_save()
		save_data['DATAID']=str(random.randint(1, 1000000000))
		write_save(save_data)
		save_data=read_save()
	except Exception:
		print("Error while loading / writing save file.")
		save_data=None
		print("Exiting the game...")
		exit()
	if save_data['BROADCAST_TYPE'] == "message":
		print("Message from devs: "+str(save_data['BROADCAST']))
		time.sleep(1)
		os.system('clear')
	try:
		listener_thread = Thread(target=keypress_listener)
		listener_thread.daemon = True
		listener_thread.start()
		drill_thread.start()
		miner_thread.start()
		send_thread.start()
		update_GUI()
		while True:
			tick()
	except KeyboardInterrupt:
		print("Game interrupted, exiting...")
		exit()
