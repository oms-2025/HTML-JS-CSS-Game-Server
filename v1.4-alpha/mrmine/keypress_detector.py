import sys
import termios
import tty
import select
import time
from contextlib import contextmanager
log_loc= '/workspaces/coolmathgames/v1.4-alpha/mrmine/log.txt'
def write_log(message):
	with open(log_loc, "a") as log_file:
		message1=('Timestamp '+ str(time.time())+': '+ str(message) + "\n")
		log_file.write(message1)
def m_kd_initialize():
	write_log('From function \'initialize\': Initializing script...')
@contextmanager
def raw_mode(file):
	old_attrs = termios.tcgetattr(file.fileno())
	try:
		tty.setraw(file.fileno())
		yield
	finally:
		termios.tcsetattr(file.fileno(), termios.TCSADRAIN, old_attrs)

SPECIAL_KEYS = {
	'\x1b[A': 'UP',
	'\x1b[B': 'DOWN',
	'\x1b[C': 'RIGHT',
	'\x1b[D': 'LEFT'
}

def detect_keypress_nonblocking():
	with raw_mode(sys.stdin):
		rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
		if rlist:
			chars = []
			char = sys.stdin.read(1)
			if char == '\x1b':  # Escape character
				chars.append(char)
				char = sys.stdin.read(1)
				if char: 
					chars.append(char)
					if char == '[':
						char = sys.stdin.read(1)
						if char:
							chars.append(char)
			result = ''.join(chars)
			return SPECIAL_KEYS.get(result, result)
	return None
