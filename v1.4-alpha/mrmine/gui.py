import os, time
global save_data
from colorama import *
log_loc= '/workspaces/coolmathgames/v1.4-alpha/mrmine/log.txt'
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
coal="""
      ██████            
    ██████████          
  ████▓▓▓▓██████        
  ████▓▓▓▓▓▓██████      
  ████▓▓▓▓▓▓▓▓██████    
████▓▓▓▓▓▓▓▓▓▓████████  
████▓▓▓▓██████████████  
████▓▓██████████████████
████████████████████████
████████████████████████
  ████████████████████  
    ████████████████    
      ██████            
"""
copper="""                                       
                                  .######*             
                                  .######*             
                        ###########*******%\%\%-         
                       .###########*******#%#-         
             *##########===+***#######****===*%\%\%      
             *##########===+***#######****===*%\%\%      
  +##%#######***+======+****#######***+======+***%\%\%+  
  +##########***+====+++***#######**+*+======++++###+  
##=---***+==========+***#######***+=======-------===+%\%
##=---+++========+++********+*++++=-=============+++*%\%
##+===---=======+**********+===-----------****######%\%@
##+=============+++++++++++=====--========***#%\%\%\###%\%@
##+===***=---=======-----------===+*******###%\%\%\%\###%@@
##+===***+===-::---===========+++++******#%\%\%\%\%\%\%***#%@
##+===###****....---+***#######*******####%\%\%\%\%\%\%***#%@
##+===#######-::-+++*#######*******####%\%\%\###%\%\%\%\%\%\%*. 
##+===#######----***#######********###%\%\%\%\###%@@@@@%*  
  +###****###---=#######*******###%\%\%\%\%\%\%\%\%\%\%=         
  +###****###----#######*******###%@@@@@@@@@%=         
     .#######====###****%\%\%\%\%\%\%\%\%\%*                    
      #######===+###****%@@@@@@@@%+                    
         -\%\#####%@@@%@%#                               
         :######%\%\%@@@@%"""
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
	1: '                * ** * **|',
	2: '                 * ** *  |',
	3: '                  ** *   |',
	4: '                    *    |',
	5: ' ================= | |   |',
	6: ' ================= | |   |',
	7: ' ||x██|██|██|██x|| | |   |',
	8: ' ||x██|██|██|██x|| | |   |',
	9: ' ||x██|██|██|██x⊥⊥_| |   |',
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
		print(coal+'\n'+save_data['MINERALS'][0])
		print(copper+'\n'+save_data['MINERALS'][1])
	elif key=="e":
		ingui=False

minerals={
#1-15 is Earth minerals, 13 max length
1: 'Coal         ',
2: 'Copper       ',
3: 'Iron         ',
4: 'Silver       ',
5: 'Gold         ',
6: 'Diamond      ',
7: 'Blue Obsidian',
8: 'Red Diamond  ',
9: 'Black Opal   ',
10: 'Californium  ',
11: 'Neodymium    ',
12: 'Titanium     ',
13: 'Uranium      ',
14: 'Plutonium    ',
15: 'Polonium     '
}
fluids={
#1-3 is earth fluids, 6 max length
1: 'Oil   ',
2: 'Fuel  ',
3: 'Energy'
}
def num_format(number):
	if number>=0 and number<10:
		return '00'+str(number)+'.00'
	elif number>=10 and number<100:
		return '0'+str(number)+'.00'
	elif number>=100 and number<1000:
		return str(number)+'.00'
	elif number>=1000 and number<10000:
		return '00'+str(round(number/1000, 1))+'K'
	elif number>=10000 and number<100000:
		return '0'+str(round(number/1000, 1))+'K'
	elif number>=100000 and number<1000000:
		return str(round(number/1000, 1))+'K'
	elif number>=1000000 and number<10000000:
		return '00'+str(round(number/1000000, 1))+"M"
	elif number>=10000000 and number<100000000:
		return '0'+str(round(number/1000000, 1))+"M"
	elif number>=100000000 and number<1000000000:
		return str(round(number/1000000, 1))+"M"
	elif number>=1000000000 and number<10000000000:
		return '00'+str(round(number/1000000000, 1))+"B"
	elif number>=10000000000 and number<100000000000:
		return '0'+str(round(number/1000000000, 1))+"B"
	elif number>=100000000000 and number<1000000000000:
		return str(round(number/1000000000, 1))+"B"
	else:
		return 'OVERFL'
def km_format(km):
	if km>=0 and km<10:
		return '000,000,00'+str(km)
	elif km>=10 and km<100:
		return '000,000,0'+str(km)
	elif km>=100 and km<1000:
		return '000,000,'+str(km)
	elif km>=1000 and km<10000:
		return '000,00'+str(km)[0]+','+str(km)[1:]
	elif km>=10000 and km<100000:
		return '000,0'+str(km)[:1]+','+str(km)[2:]
	elif km>=100000 and km<1000000:
		return '000,'+str(km)[:2]+','+str(km)[3:]
	elif km>=1000000 and km<10000000:
		return '00'+str(km)[0]+','+str(km)[1::3]+','+str(km)[4:]
	elif km>=10000000 and km<100000000:
		return '0'+str(km)[:1]+','+str(km)[2::4]+','+str(km)[5:]
	elif km>=100000000 and km<1000000000:
		return str(km)[:2]+','+str(km)[3::5]+','+str(km)[6:]
	else:
		return 'OVERFLOW_ER'
def percent_format(percent):
	return str(percent)+(' '*(5-len(str(percent))))
def print_top_gui():
	global save_data
	try:
		planet_offset_15 = (save_data['PLANET'] - 1) * 15
		planet_offset_3 = (save_data['PLANET'] - 1) * 3
		top_gui = f"""===================================================================================================================================================="""+'\r'+'\n'+f"""| {str(num_format(save_data['MINERALS'][0]))} {minerals[1 + planet_offset_15]}   {str(num_format(save_data['MINERALS'][3]))} {minerals[4 + planet_offset_15]}   {str(num_format(save_data['MINERALS'][6]))} {minerals[7 + planet_offset_15]}   {str(num_format(save_data['MINERALS'][9]))} {minerals[10 + planet_offset_15]}   {str(num_format(save_data['MINERALS'][12]))} {minerals[13 + planet_offset_15]}   {str(num_format(save_data['FLUIDS'][0]))} {fluids[1 + planet_offset_3]}   ${str(num_format(save_data['MONEY']))} money |"""+'\r'+'\n'+f"""| {str(num_format(save_data['MINERALS'][1]))} {minerals[2 + planet_offset_15]}   {str(num_format(save_data['MINERALS'][4]))} {minerals[5 + planet_offset_15]}   {str(num_format(save_data['MINERALS'][7]))} {minerals[8 + planet_offset_15]}   {str(num_format(save_data['MINERALS'][10]))} {minerals[11 + planet_offset_15]}   {str(num_format(save_data['MINERALS'][13]))} {minerals[14 + planet_offset_15]}   {str(num_format(save_data['FLUIDS'][1]))} {fluids[2 + planet_offset_3]}   {str(km_format(save_data['DEPTH']))}KM |"""+'\r'+'\n'+f"""| {str(num_format(save_data['MINERALS'][2]))} {minerals[3 + planet_offset_15]}   {str(num_format(save_data['MINERALS'][5]))} {minerals[6 + planet_offset_15]}   {str(num_format(save_data['MINERALS'][8]))} {minerals[9 + planet_offset_15]}   {str(num_format(save_data['MINERALS'][11]))} {minerals[12 + planet_offset_15]}   {str(num_format(save_data['MINERALS'][14]))} {minerals[15 + planet_offset_15]}   {str(num_format(save_data['FLUIDS'][2]))} {fluids[3 + planet_offset_3]}   ({str(percent_format(GUI_data['PERCENT_TO_NEW_LAYER']))}% done) |"""
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
					print('\r'+'=========================================================================================================================|                         |')
					print('\r'+'| '+str(km_number2)+' KM \\     /        \\     /        \\     /           \\     /           \\     /        \\     /        \\     /        |                         |')
					print('\r'+'|          \\   /          \\   /          \\   /             \\   /             \\   /          \\   /          \\   /         |                         |')
					print('\r'+'|           \\ /            \\ /            \\ /               \\ /               \\ /            \\ /            \\ /          |                         |')
					print('\r'+'|            X              X              X                 X                 X              X              X           |'+drill[1])
					print('\r'+'|           / \\            / \\            / \\               / \\               / \\            / \\            / \\          |'+drill[2])
					print('\r'+'|          /   \\          /   \\          /   \\             /   \\             /   \\          /   \\          /   \\         |'+drill[3])
					print('\r'+'|         /     \\        /     \\        /     \\           /     \\           /     \\        /     \\        /     \\        |'+drill[4])
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
