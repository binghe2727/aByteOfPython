#useingSys.py
import sys

def readFile(filename):
	'''print something'''
	f=file(filename)
	while True:
		line=f.readline()
		if len(line)==0:
			break
		print line,#notice the comma
	f.close()

if len(sys.argv)<2:
	print 'No action specified'
	sys.exit()

if sys.argv[1].startswith('--'):
	option=sys.argv[1][2:]
	if option=='version':
		print 'Version 1.2'
	elif option=='help':
		print '''\
	ths program
	--version
	--help'''
	else:
		print 'Unknown operations'
	sys.exit()
else:
	for filename in sys.argv[1:]:
		readFile(filename)