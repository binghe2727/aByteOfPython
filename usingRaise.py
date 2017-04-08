# -*- coding: utf-8 -*
#using the raising.py
class ShortInputException(Exception):
	"""docstring for ShortInputException"""
	def __init__(self, length,atleast):
		Exception.__init__(self)
		self.length = length
		self.atleast=atleast
try:
	s=raw_input('enter soemthing-->')
	if len(s)<3:
		raise ShortInputException(len(s),3)
		#other can continue as usual here
except EOFError:
	print 'why eof on me'
except ShortInputException,x:
	print 'ShortInputExcepton: The input was of length%d,\
	was expectiong at least %d'%(x.length,x.atleast)
#except ShortInputException:
#	print 'ShortInputExcepton: The input was of length%d,\
#	was expectiong at least %d'%(ShortInputException.length,ShortInputException.atleast)
#原本的这样不运行，因为，还是没有实例化对应的error相关特性，这样的，只是调用了class name ,
#没有启用具体的参数调用
else:
	print 'No exception'
