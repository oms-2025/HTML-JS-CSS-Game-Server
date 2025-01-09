from threading import Thread
import threading
from mrmine.keypress_detector import detect_keypress_nonblocking
from mrmine.gui import update_GUI, scroll, update_GUI_func, GUI_send, get_save
from mrmine.save import *
from mrmine.chest import *
from mrmine.html import *
import os, time, random, math
global save_data, ret
# Make the relay of keys more accessible
version='v1.5-alpha.3'
key_pressed = None
log_loc= '/workspaces/coolmathgames/v1.5-alpha.3/mrmine/log.txt'
def get_reactor_rate():
	pass
	return 1
def write_log(message):
	with open(log_loc, "a") as log_file:
		message1=('Timestamp '+ str(time.time())+': '+ str(message) + "\n")
		log_file.write(message1)
def m_ms_initialize():
	write_log('From function \'initialize\': Initializing script...')
def keypress_listener():
	global key_pressed
	while True:
		key_pressed = detect_keypress_nonblocking()
		if key_pressed:
			write_log(f'Key pressed: {key_pressed}')
			# Add a break condition or some logic to exit the loop
			break
def chest_generate():
	while True:
		time.sleep(30)
		chest_roll=generate_chest(save_data['DEPTH'])
		if chest_roll[0]!='none':
			save_data['CHEST_DATA'].append(chest_roll)
			write_log(f'From function \'chest_generate\': Generating chest with data {chest_roll}...')
chest_thread=threading.Thread(target=chest_generate)
def tick():
	global key_pressed
	minerals={
#earth minerals
1: 'Coal         ',
2: 'Copper       ',
3: 'Silver       ',
4: 'Gold         ',
5: 'Platinum     ',
6: 'Diamond      ',
7: 'Coltan       ',
8: 'Painite      ',
9: 'Black Opal   ',
10: 'Red Diamond  ',
11: 'Blue Obsidian',
12: 'Californium  ',
#earth isotopes
13: 'Uranium-1    ',
14: 'Uranium-2    ',
15: 'Uranium-3    ',
16: 'Plutonium-1  ',
17: 'Plutonium-2  ',
18: 'Plutonium-3  ',
19: 'Polonium-1   ',
20: 'Polonium-2   ',
21: 'Polonium-3   ',
#moon minerals
22: 'Carbon       ',
23: 'Iron         ',
24: 'Aluminium    ',
25: 'Magnesium    ',
26: 'Titanium     ',
27: 'Silicon      ',
28: 'Promethium   ',
29: 'Neodymium    ',
30: 'Ytterbium    ',
#moon isotopes
31: 'Nitrogen-1   ',
32: 'Nitrogen-2   ',
33: 'Nitrogen-3   ',
34: 'Helium-1     ',
35: 'Helium-2     ',
36: 'Helium-3     ',
37: 'Einsteinium-1',
38: 'Einsteinium-2',
39: 'Einsteinium-3',
40: 'Fermium-1    ',
41: 'Fermium-2    ',
42: 'Fermium-3    ',
#titan minerals
43: 'Tin          ',
44: 'Sulfur       ',
45: 'Lithium      ',
46: 'Manganese    ',
47: 'Mercury      ',
48: 'Nickel       ',
49: 'Alexandrite  ',
50: 'Benitoite    ',
51: 'Cobalt       ',
#titan isotopes
52: 'Hydrogen-1   ',
53: 'Hydrogen-2   ',
54: 'Hydrogen-3   ',
55: 'Oxygen-1     ',
56: 'Oxygen-2     ',
57: 'Oxygen-3     '
	}
	save_data['UNLOCKED']=[]
	for (key, mineral) in minerals:
		if save_data['MINERALS'][key]>0:
			save_data['UNLOCKED'].append(mineral)
	while True:
		if key_pressed:
			key = key_pressed
			key_pressed = False
			print(f"Key registered: {key}")
			if key == 'up' or key == 'down':
				scroll(key)
				update_GUI()
			elif key in ["k", "q", "c", "s", "h", "u", " ", "p", "r", "e"]:
				update_GUI_func(key)
		else:
			time.sleep(0.1)
			update_GUI()
mins={
#earth minerals
1: 0,
2: 4,
3: 13,
4: 17,
5: 21,
6: 30,
7: 45,
8: 60,
9: 79,
10: 80,
11: 93,
12: 305,
#earth isotopes
13: 24,
14: 24,
15: 24,
16: 34,
17: 34,
18: 34,
19: 54,
20: 54,
21: 54,
#moon minerals
22: 1032,
23: 1041,
24: 1045,
25: 1125,
26: 1211,
27: 1342,
28: 1462,
29: 1562,
30: 1632,
#moon isotopes
31: 1067,
32: 1067,
33: 1067,
34: 1132,
35: 1132,
36: 1132,
37: 'reactor',
38: 'reactor',
39: 'reactor',
40: 'reactor',
41: 'reactor',
42: 'reactor',
#titan minerals
43: 1814,
44: 1854,
45: 1878,
46: 2015,
47: 2142,
48: 2170,
49: 2384,
50: 2347,
51: 2581,
#titan isotopes
52: 1849,
53: 1849,
54: 1849,
55: 1914,
56: 1914,
57: 1914
}
sines={
1: 0.448,
2: 0.346,
3: 0.39,
4: 0.2,
5: 0.116,
6: 0.106,
7: 0.101,
8: 0.0995,
9: 0.0434,
10: 0.0161,
11: 0.008799,
12: 0.0079525,
#earth isotopes
13: 0,
14: 0,
15: 0,
16: 0,
17: 0,
18: 0,
19: 0,
20: 0,
21: 0,
#moon minerals
22: 0.0313,
23: 0.0313,
24: 0.0313,
25: 0.0313,
26: 0.03,
27: 0.04167,
28: 0.0698,
29: 0.059,
30: 0.0336,
#moon isotopes
31: 0,
32: 0,
33: 0,
34: 0,
35: 0,
36: 0,
37: 0,
38: 0,
39: 0,
40: 0,
41: 0,
42: 0,
#titan minerals
43: 0.052,
44: 0.052,
45: 0.052,
46: 0.049,
47: 0.045,
48: 0.045,
49: 0.042,
50: 0.042,
51: 0.042,
#titan isotopes
52: 0,
53: 0,
54: 0,
55: 0,
56: 0,
57: 0
}
ideals={
#earth minerals
1: 7,
2: 13,
3: 21,
4: 32.5,
5: 48,
6: 59.5,
7: 76,
8: 91.5,
9: 151,
10: 275,
11: 450,
12: 700,
#earth isotopes
13: 24,
14: 244,
15: 2444,
16: 34,
17: 344,
18: 3444,
19: 54,
20: 544,
21: 5444,
#2oon minerals
22: 1132,
23: 1141,
24: 1145,
25: 1225,
26: 1315,
27: 1417,
28: 1507,
29: 1615,
30: 1725,
#2oon isotopes
31: 1067,
32: 10677,
33: 106777,
34: 1132,
35: 11322,
36: 113222,
37: 'reactor',
38: 'reactor',
39: 'reactor',
40: 'reactor',
41: 'reactor',
42: 'reactor',
#titan minerals
43: 1864,
44: 1914,
45: 1938,
46: 2079,
47: 2142,
48: 2273,
49: 2413,
50: 2541,
51: 2668,
#titan isotopes
52: 1849,
53: 18499,
54: 184999,
55: 1914,
56: 19144,
57: 191444
}
def check_html():
	global ret
	start=time.time()
	ret=''
	while ret=='':
		ret=checkhtmldata()
		if time.time()-start>=60:
			write_log('From function \'check_html\': Timeout while getting data from HTML input')
			exit()
check_thread = threading.Thread(target=check_html)
def drill_percent():
	global save_data
	while True:
		drill_data=save_data['DRILL_DATA']
		time_to_new_depth=save_data['LAYER_HARDNESS']/drill_data[0]
		start_new_depth=time.time()
		end_new_depth=start_new_depth+time_to_new_depth
		while time.time()<=end_new_depth:
			percent=round(((time.time()-start_new_depth)/time_to_new_depth)*100, 2)
			GUI_send(percent, "percent_to_new_layer")
			time.sleep(0.1)
		save_data['DEPTH']+=1
		if save_data['DIFFICULTY']==1:
			save_data['LAYER_HARDNESS']=float((1.57**(1+(save_data['DEPTH']/50)))+23.43)
		elif save_data['DIFFICULTY']==2:
			save_data['LAYER_HARDNESS']=float((0.527*(save_data['DEPTH']**2.168))+30)
		elif save_data['DIFFICULTY']==3:
			save_data['LAYER_HARDNESS']=float((save_data['DEPTH']**2.168)+30)
		else:
			save_data['LAYER_HARDNESS']=float((1.57**(1+(save_data['DEPTH']/50)))+23.43)
		write_log(f'From function \'drill_percent\': new layer; new hardness is {save_data['LAYER_HARDNESS']}.')
def miner_monitor():
	global save_data, ideals, mins
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
		15: 0,
		16: 0,
		17: 0,
		18: 0,
		19: 0,
		20: 0,
		21: 0,
		22: 0,
		23: 0,
		24: 0,
		25: 0,
		26: 0,
		27: 0,
		28: 0,
		29: 0,
		30: 0,
		31: 0,
		32: 0,
		33: 0,
		34: 0,
		35: 0,
		36: 0,
		37: 0,
		38: 0,
		39: 0,
		40: 0,
		41: 0,
		42: 0,
		43: 0,
		44: 0,
		45: 0,
		46: 0,
		47: 0,
		48: 0,
		49: 0,
		50: 0,
		51: 0,
		52: 0,
		53: 0,
		54: 0,
		55: 0,
		56: 0,
		57: 0
		}
		isotopes=[24, 244, 2444, 34, 344, 3444, 54, 544, 5444, 1067, 10677, 106777, 1132, 11322, 113222, 1849, 18499, 184999, 1914, 19144, 191444]
		isotope_rates=[0.03, 0.02, 0.01, 0.02, 0.01, 0.006, 0.01, 0.006, 0.003, 0.02, 0.01, 0.006, 0.005, 0.003, 0.001, 0.01, 0.006, 0.002, 0.002, 0.001, 0.0006]
		while i<=save_data['DEPTH']:
			mnum=1
			while mnum<=57:
				if ideals[mnum]=='reactor':
					resource_input[mnum]+=get_reactor_rate(mnum)
					if ideals[mnum] in isotopes:
						resource_input[mnum]+=isotope_rates[mnum]
					else:
						if i>=mins[mnum]:
							if abs(i-ideals[mnum])<=30:
								richness=((0.5*math.sin((sines[mnum]*i)+1.571))+0.5)
							else:
								richness=0.001
							mnum+=1
							resource_input[mnum]+=richness
			i+=1
		for mineral in resource_input:
			save_data['MINERALS'][mineral-1]+=resource_input[mineral]
			save_data['MINERALS'][mineral-1]=int(round(save_data['MINERALS'][mineral-1], 6))
		time.sleep(0.1)
drill_thread=threading.Thread(target=drill_percent)
miner_thread=threading.Thread(target=miner_monitor)
def send_data_to_GUI():
	while True:
		get_save(save_data)
		time.sleep(0.02)
send_thread=threading.Thread(target=send_data_to_GUI)
def clear_log():
	with open(log_loc, "w"):
		write_log('From function \'clear_log\': clearing log file')
keys=['v2bt7714']
def mrmine_start_game():
	clear_log()
	global save_data
	os.system('clear')
	try:
		save_data=read_save('/workspaces/coolmathgames/v1.5-alpha.3/mrmine/mrmine_save.txt')
		save_data['DATAID']=random.randint(1, 1000000000)
		write_save(save_data, '/workspaces/coolmathgames/v1.5-alpha.3/mrmine/mrmine_save.txt')
	except Exception as e:
		write_log(e)
		print("Error while loading / writing save file.")
		#save_data=None
		#print("Exiting the game...")
		#exit()
		print("Using template data...")
		save_data = {
'SAVE_NUMBER': 1,
'END_TIME': 0,
'STORAGE': 0,
'UPGRADES': [],
'MINERALS': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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
'DEPTH': 4,
'DRILL_DATA': [1, 1],
'RIG_DATA': [],
'LAYER_HARDNESS': 1,
'FORGE_STATUS': 'none',
'BROADCAST': '',
'BROADCAST_TYPE': 'none',
'DATAID': 0,
'PLANET': 1,
'DIFFICULTY': 1,
'UNLOCKED': ['Coal', 'Copper', 'Silver'],
'REACTOR_DATA': [],
'NAME': ''
		}
	write_log('From function \'mrmine_start_game\': Verifying save file integrity...')
	if save_data['VERSION']!=version:
		print('Your save file is on the wrong version. Compatibility issues may arise. Please download the newest version of the game or find a compatible save file.')
		write_log('From function \'mrmine_start_game\': Invalid save file version.')
		cont=input('Would you like the game to continue running? [You may corrupt your save or cause fatal errors.] > ')
		yes=['yes', 'y']
		if cont.lower() in yes:
			print('Continuing with game...')
			write_log('From function \'mrmine_start_game\': Continuing game from user input.')
			time.sleep(0.5)
		else:
			print('Exiting game...')
			write_log('From function \'mrmine_start_game\': Exiting game from user input.')
	else:
		write_log('From function \'mrmine_save_game\': Save file integrity verified.')
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
		chest_thread.start()
		writehtml(0, None)
		check_thread.start()
		check_thread.join()
		if ret[0] in keys:
			save_data['NAME']=ret[1]
		else:
			write_log('From function \'mrmine_start_game\': invalid key input from HTML')
		update_GUI()
		while True:
			tick()
	except KeyboardInterrupt:
		print("Game interrupted, exiting...")
		exit()