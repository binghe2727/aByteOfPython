# -*- coding: utf-8 -*
#usingThefile.py
peom='''\
Programming is fun 
by using Pyhon\
something'''#进一步理解物理行，就是看到每一行，而逻辑行，就是python默认运行的行数
#而在实际的运行中，Python认为每个物理行，就是一个运行的逻辑航，当
#需要进行对应的多行书写的时候，就需要注释对应的\ 对应的物理行，以此为基础
#进行进一步的展开运用分析。
f=file('poem.txt','w')#w for writing
f.write(peom)
f.close()

f=file('poem.txt','r')#no specified,using the default r to read
while True:
	line=f.readline()#这里的readline还是按照物理行来读取，这个要注意
	#readline就是读取的对应行
	if len(line)==0:
		break
	print line,#comma to avoid new line
f.close()
#help(file)