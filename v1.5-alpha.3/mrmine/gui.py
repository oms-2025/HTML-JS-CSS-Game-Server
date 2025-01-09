import os, time
global save_data
from colorama import *
from mrmine.sprites import get_sprite
log_loc= '/workspaces/coolmathgames/v1.5-alpha.3/mrmine/log.txt'
def write_log(message):
	with open(log_loc, "a") as log_file:
		message1=('Timestamp '+ str(time.time())+': '+ str(message) + "\n")
		log_file.write(message1)
def m_g_initialize():
	write_log('From function \'initialize\': Initializing script...')
GUI_data={
'VIEW_DEPTH': 2,
'TOP_DEPTH': 0,
'BOTTOM_DEPTH': 4,
'PERCENT_TO_NEW_LAYER': 0
}
ingui=False
progress={
	1: '\u2590',
	2: '\u259f',
	3: '\u2599',
	4: '\u258c',
	5: '\u259b',
	6: '\u259c'
}
drill={ 
	1:  '                * ** * **|',
	2:  '                 * ** *  |',
	3:  '                  ** *   |',
	4:  '                    *    |',
	5:  ' ================= | |   |',
	6:  ' ================= | |   |',
	7:  ' ||x██|██|██|██x|| | |   |',
	8:  ' ||x██|██|██|██x|| | |   |',
	9:  ' ||x██|██|██|██x⊥⊥_| |   |',
	10: ' ||x██|██|██|██x_____|   |',
	11: ' ||x██|██|██|██x||       |',
	12: ' \\\\=*=*=*=*=*=*=//       |',
	13: '  \\\\=*=*=*=*=*=//        |',
	14: '   \\\\=*=*=*=*=//         |',
	15: '    \\\\=*=*=*=//          |',
	16: '     \\\\=*=*=//           |',
	17: '      \\\\=*=//            |',
	18: '       \\\\=//             |',
	19: '        \\|/              |',
	20: '         |               |'
}
exhaust={
	1: '  *  █**  *  * █* *  ** *|',
	2: '   *█ * **█ *█* *  * *  *|',
	3: '    * █ *█* **█ * **  *  |',  
	4: '   \\\\* █* *█ █*//* **  * |',
	5: '    \\\\█* *█ █*//* ** * **|',
	6: '     \\\\█|██|█//  * ** *  |',
	7: '     //██||██\\\\   ** *   |',
	8: '    //██|██|██\\\\    *    |'
}
icons={
	1: (Style.DIM+Fore.WHITE+"""
===============
|  D R I L L  |
| L E V E L 1 |
|   \\\\=*=//   |
|    \\\\=//   |
|     \\|/     |
|      |      |
===============""")
}

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
def get_save(data):
	global save_data
	save_data=data
	GUI_data['BOTTOM_DEPTH']=save_data['DEPTH']
value={
	#earth minerals
	1: 1,
	2: 2,
	3: 4,
	4: 16,
	5: 32,
	6: 64,
	7: 500,
	8: 1000,
	9: 2000,
	10: 10000,
	11: 20000,
	12: 100000,
	#earth isotopes
	13: 100,
	14: 2000,
	15: 50000,
	16: 1000,
	17: 20000,
	18: 500000,
	19: 5000,
	20: 250000,
	21: 50000000,
	#moon minerals
	22: 500000,
	23: 1000000,
	24: 2000000,
	25: 5000000,
	26: 750000000,
	27: 100000000,
	28: 1400000000,
	29: 10000000000,
	30: 50000000000,
	#moon isotopes
	31: 50000000,
	32: 150000000,
	33: 300000000,
	34: 500000000,
	35: 5000000000,
	36: 500000000000,
	37: 550000000000,
	38: 5500000000000,
	39: 550000000000000,
	40: 66600000000000,
	41: 246000000000000,
	42: 6960000000000000,
	#titan minerals
	43: 500000000000,
	44: 2500000000000,
	45: 10000000000000,
	46: 750000000000000,
	47: 7500000000000000,
	#end of titan implementations
	48: 15000000000000000,
	49: 30000000000000000,
	50: 120000000000000000,
	51: 360000000000000000,
	#titan isotopes
	52: 50000000000000,
	53: 500000000000000,
	54: 5000000000000000,
	55: 66600000000000,
	56: 666000000000000,
	57: 6660000000000000
}
unlocked=['coal', 'copper', 'silver']
def update_GUI_func(key):
	global ingui
	if key=='q':
		os.system('clear')
		print("""
|==================================================================================================================================================|
|                                                                                                                                                  |
|   |==========================================================================================================================================|   |
|   |                                     /========    =========         /\\        |=========    ==========                                    |   |
|   |                                    |             |       |        /  \\       |                 ||                                        |   |
|   |                                    |             |_______/       /____\\      |=========        ||                                        |   |
|   |                                    |             |       \\      /      \\     |                 ||                                        |   |
|   |                                     \\========    |        \\    /        \\    |                 ||                                        |   |
|   |                                                                                                                                          |   |
|   |                                                                                                                                          |   |
|   |                                                                                                                                          |   |
|   |                                                                                                                                          |   |
|   |                                                                                                                                          |   |
|   |                                                                                                                                          |   |
|   |                                                                                                                                          |   |
|   |                                                                                                                                          |   |
|   |                                                                                                                                          |   |
|   |                                                                                                                                          |   |
|   |                                                                                                                                          |   |
|   |                                                                                                                                          |   |
|   |                                                                                                                                          |   |
|   |                                                                                                                                          |   |
|   |                                                                                                                                          |   |
|   |                                                                                                                                          |   |
|   |                                                                                                                                          |   |
|   |                                                                                                                                          |   |
|   |                                                                                                                                          |   |
|   |                                                                                                                                          |   |
|   |                                                                                                                                          |   |
|   |                                                                                                                                          |   |
|   |                                                                                                                                          |   |
|   |                                                                                                                                          |   |
|   |                                                                                                                                          |   |
|   |                                                                                                                                          |   |
|   |                                                                                                                                          |   |
|   |                                                                                                                                          |   |
|   |                                                                                                                                          |   |
|   |==========================================================================================================================================|   |
|                                                                                                                                                  |
|==================================================================================================================================================|""")
	elif key=='s':
		ingui=True
		os.system('clear')
		i=1
		while i<=len(unlocked):
			print(get_sprite(i)+'\n'+save_data['MINERALS'][0])
			i+=1
		mineral=input('What mineral would you like to sell? (1-60) > ').lower()
		if mineral>=1 and mineral<=len(unlocked):
			if mineral in minerals:
				amount=input(f'How much of that mineral would you like to sell? > ')
			print(f'Attempting to sell {amount} units of {minerals[mineral]}...')
			time.sleep(1)
			try:
				if save_data['MINERALS'][mineral]>=amount:
					save_data['MINERALS'][mineral]-=amount
					save_data['MONEY']+=amount*value[mineral]
					print("Successfully sold!")
			except Exception as e:
				print('Invalid input.')
				write_log(f'From function \'update_GUI_func\': Error while selling mineral; traceback {e}.')
		else:
			print("Mineral is not unlocked.")
	elif key=="e":
		ingui=False

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
fluids={
#1-3 is earth fluids, 6 max length
1: 'Oil   ',
2: 'Fuel  ',
3: 'Energy'
}
def num_format(num):
    suffixes = ["  ", "K ", "M ", "B ", "T ", "Qa", "Qi", "Sx", "Sp", "Oc", "No", "De", "Un", "Du", "Tr", "Qu", "Qn", "Sd", "St", "Ot", "Nv", "Vi"]
    num_length = len(suffixes)

    index = 0
    while abs(num) >= 1000 and index < num_length - 1:
        num /= 1000.0
        index += 1

    # Ensure the formatted number including its suffix fits within 6 characters
    return f"{num:06.1f}{suffixes[index]}"
def km_format(km):
    try:
        if km < 0:
            return 'NEGATIVE_ER'
        num_str = f"{km:.0f}"
        while len(num_str) < 9:
            num_str = '0' + num_str
            
        formatted = f"{num_str[-9:-6]},{num_str[-6:-3]},{num_str[-3:]}"
        return formatted
    except (ValueError, TypeError) as e:
        return 'OVERFLOW_ER'
line_separator = "=" * 180

def format_resource_line(mineral_indices, fluid_index, suffix, planet_offset_3, planet_offset_15):
    return (
        f"| {str(num_format(save_data['MINERALS'][mineral_indices[0]]))} {minerals[mineral_indices[1] + planet_offset_15]}   "
        f"{str(num_format(save_data['MINERALS'][mineral_indices[2]]))} {minerals[mineral_indices[3] + planet_offset_15]}   "
        f"{str(num_format(save_data['MINERALS'][mineral_indices[4]]))} {minerals[mineral_indices[5] + planet_offset_15]}   "
        f"{str(num_format(save_data['MINERALS'][mineral_indices[6]]))} {minerals[mineral_indices[7] + planet_offset_15]}   "
        f"{str(num_format(save_data['MINERALS'][mineral_indices[8]]))} {minerals[mineral_indices[9] + planet_offset_15]}   "
        f"{str(num_format(save_data['FLUIDS'][fluid_index]))} {fluids[fluid_index + planet_offset_3]}   "
        f"{suffix} |"
    )
def inspace():
	if save_data['DEPTH'] in range(1001, 1031) or save_data['DEPTH'] in range(1783, 1813):
		return True
	else:
		return False

def percent_format(percent):
	return str(percent)+(' '*(5-len(str(percent))))
def print_top_gui():
	global save_data
	try:
		if GUI_data['VIEW_DEPTH']<=1000:
			planet=1
		elif GUI_data['VIEW_DEPTH']<=1782:
			planet=2
		elif GUI_data['VIEW_DEPTH']<=2214:
			planet=3
		planet_offset_3=(planet-1)*3
		planet_offset_15=(planet-1)*15
		top_gui = (
		f"{line_separator}\r\n"
		+ format_resource_line([0, 1, 3, 4, 6, 7, 9, 10, 12, 13], 0, f"${str(num_format(save_data['MONEY']))} money", planet_offset_3, planet_offset_15) + '\r\n'
		+ format_resource_line([1, 2, 4, 5, 7, 8, 10, 11, 13, 14], 1, f"{str(km_format(save_data['DEPTH']))}KM", planet_offset_3, planet_offset_15) + '\r\n'
		+ format_resource_line([2, 3, 5, 6, 8, 9, 11, 12, 14, 15], 2, f"({str(percent_format(GUI_data['PERCENT_TO_NEW_LAYER']))}% done)", planet_offset_3, planet_offset_15)
		)
		print('\r' + top_gui)
	except Exception as e:
		print(e)
def update_GUI():
	if not ingui:
		os.system('clear')
		print_top_gui()
		if GUI_data['VIEW_DEPTH']==2:
			print('\r'+'====================================================================================================================================================')
			print('\r'+'| 0000 KM                                                                                                                |                         |')
			print('\r'+'|                                                                                                                        |                         |')
			print('\r'+'|          =========                   =========                   =========                   =========                 |                         |')
			print('\r'+'|         //       \\\\                 //       \\\\                 //       \\\\                 //       \\\\                |                         |')
			print('\r'+'|        //         \\\\               //         \\\\               //         \\\\               //         \\\\               |                         |')
			print('\r'+'|       ||  S E L L  ||             ||  H I R E  ||             || C R A F T ||             || Q U E S T ||              |                         |')
			print('\r'+'|       ||           ||             ||           ||             ||           ||             ||           ||              |                         |')
		if GUI_data['BOTTOM_DEPTH']>=4 and GUI_data['VIEW_DEPTH']>=2:
			depths=[]
			if GUI_data['VIEW_DEPTH']>=3:
				i=0
			else:
				i=1
			while i<=4:
				depths.append(GUI_data['VIEW_DEPTH']-2+i)
				i+=1
			km_number=0
			for depth in depths:
				if depth<10:
					km_number=str('000'+str(depth))
				elif depth>=10 and depth<100:
					km_number=str('00'+str(depth))
				elif depth>=100 and depth<1000:
					km_number=str('0'+str(depth))
				elif depth>=1000 and depth<10000:
					km_number=str(depth)
				else:
					km_number=str(depth)
					print("DEPTH LIMIT EXCEEDED")
				km_number2=km_number
				km_number=int(km_number)
				if km_number<=GUI_data['BOTTOM_DEPTH']-3:
					print('\r'+'=========================================================================================================================|                         |')
					print('\r'+'| '+str(km_number2)+' KM \\     /        \\     /        \\     /           \\     /           \\     /        \\     /        \\     /        |                         |')
					print('\r'+'|          \\   /          \\   /          \\   /             \\   /             \\   /          \\   /          \\   /         |                         |')
					print('\r'+'|           \\ /            \\ /            \\ /               \\ /               \\ /            \\ /            \\ /          |                         |')
					print('\r'+'|            X              X              X                 X                 X              X              X           |                         |')
					print('\r'+'|           / \\            / \\            / \\               / \\               / \\            / \\            / \\          |                         |')
					print('\r'+'|          /   \\          /   \\          /   \\             /   \\             /   \\          /   \\          /   \\         |                         |')
					print('\r'+'|         /     \\        /     \\        /     \\           /     \\           /     \\        /     \\        /     \\        |                         |')
				elif km_number==GUI_data['BOTTOM_DEPTH']-2:
					if inspace():
						print('\r'+'=========================================================================================================================|                         |')
						print('\r'+'| '+str(km_number2)+' KM \\     /        \\     /        \\     /           \\     /           \\     /        \\     /        \\     /        |                         |')
						print('\r'+'|          \\   /          \\   /          \\   /             \\   /             \\   /          \\   /          \\   /         |                         |')
						print('\r'+'|           \\ /            \\ /            \\ /               \\ /               \\ /            \\ /            \\ /          |                         |')
						print('\r'+'|            X              X              X                 X                 X              X              X           |'+drill[1])
						print('\r'+'|           / \\            / \\            / \\               / \\               / \\            / \\            / \\          |'+drill[2])
						print('\r'+'|          /   \\          /   \\          /   \\             /   \\             /   \\          /   \\          /   \\         |'+drill[3])
						print('\r'+'|         /     \\        /     \\        /     \\           /     \\           /     \\        /     \\        /     \\        |'+drill[4])
					else:
						print('\r'+'=========================================================================================================================|                         |'+exhaust[1])
						print('\r'+'| '+str(km_number2)+' KM \\     /        \\     /        \\     /           \\     /           \\     /        \\     /        \\     /        |                         |'+exhaust[2])
						print('\r'+'|          \\   /          \\   /          \\   /             \\   /             \\   /          \\   /          \\   /         |                         |'+exhaust[3])
						print('\r'+'|           \\ /            \\ /            \\ /               \\ /               \\ /            \\ /            \\ /          |                         |'+exhaust[4])
						print('\r'+'|            X              X              X                 X                 X              X              X           |'+exhaust[5])
						print('\r'+'|           / \\            / \\            / \\               / \\               / \\            / \\            / \\          |'+exhaust[6])
						print('\r'+'|          /   \\          /   \\          /   \\             /   \\             /   \\          /   \\          /   \\         |'+exhaust[7])
						print('\r'+'|         /     \\        /     \\        /     \\           /     \\           /     \\        /     \\        /     \\        |'+exhaust[8])
				elif km_number==GUI_data['BOTTOM_DEPTH']-1:
					print('\r'+'=========================================================================================================================|'+drill[5])
					print('\r'+'| '+str(km_number2)+' KM \\     /        \\     /        \\     /           \\     /           \\     /        \\     /        \\     /        |'+drill[6])
					print('\r'+'|          \\   /          \\   /          \\   /             \\   /             \\   /          \\   /          \\   /         |'+drill[7])
					print('\r'+'|           \\ /            \\ /            \\ /               \\ /               \\ /            \\ /            \\ /          |'+drill[8])
					print('\r'+'|            X              X              X                 X                 X              X              X           |'+drill[9])
					print('\r'+'|           / \\            / \\            / \\               / \\               / \\            / \\            / \\          |'+drill[10])
					print('\r'+'|          /   \\          /   \\          /   \\             /   \\             /   \\          /   \\          /   \\         |'+drill[11])
					print('\r'+'|         /     \\        /     \\        /     \\           /     \\           /     \\        /     \\        /     \\        |'+drill[12])
				elif km_number==GUI_data['BOTTOM_DEPTH']:
					print('\r'+'=========================================================================================================================|'+drill[13])
					print('\r'+'| '+str(km_number2)+' KM \\     /        \\     /        \\     /           \\     /           \\     /        \\     /        \\     /        |'+drill[14])
					print('\r'+'|          \\   /          \\   /          \\   /             \\   /             \\   /          \\   /          \\   /         |'+drill[15])
					print('\r'+'|           \\ /            \\ /            \\ /               \\ /               \\ /            \\ /            \\ /          |'+drill[16])
					print('\r'+'|            X              X              X                 X                 X              X              X           |'+drill[17])
					print('\r'+'|           / \\            / \\            / \\               / \\               / \\            / \\            / \\          |'+drill[18])
					print('\r'+'|          /   \\          /   \\          /   \\             /   \\             /   \\          /   \\          /   \\         |'+drill[19])
					print('\r'+'|         /     \\        /     \\        /     \\           /     \\           /     \\        /     \\        /     \\        |'+drill[20])
			if km_number==GUI_data['BOTTOM_DEPTH']:
				print('\r'+'====================================================================================================================================================')
			else:
				print('\r'+'====================================================================================================================================================')
def scroll(key):
	if key=='up':
		if GUI_data['VIEW_DEPTH']>=3:
			GUI_data['VIEW_DEPTH']-=1
	elif key=='down':
		if GUI_data['VIEW_DEPTH']<=GUI_data['BOTTOM_DEPTH']-3:
			GUI_data['VIEW_DEPTH']+=1
def GUI_send(data, type):
	if type=="percent_to_new_layer":
		GUI_data['PERCENT_TO_NEW_LAYER']=data
	elif type=='signal':
		pass