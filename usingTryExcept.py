#tryExcept.py
import sys
try:
	s=raw_input('enter something------')
	print 'put finish'
except EOFError:
	print '\nwhy do eof'
	sys.exit()
except:
	print '\n something wrong'
print 'Done'