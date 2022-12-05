#!/usr/bin/python3
from sys import argv
if __name__ == '__main__'
	argc = ((len(argv))-1)
	print(argc, end='')
	if argc == 0:
		print(' arguments.')
	elif argc == 1:
		print(' argument:')
	else:
		print(' arguments:')
	for cnt, arg in enumerate(argv):
		if cnt == 0:
			continue
		else:
			print(f'{str(cnt).rstrip()}: {arg}')
