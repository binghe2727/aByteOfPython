# -*- coding: utf-8 -*
import cPickle as p
#import pickle as p
shopListFile='shopList.data'
#the name of the file to store the object
shopList=['apple','mango','carrot']
#write to this file
f=file(shopListFile,'w')#注意，自己第一次coding的时候，没有注意
#打字成了shopList竟然还查错很久，不仅仅要对着比照，也要进行理解，
#不要死记硬背，这样非常的不好。务必注意体会
p.dump(shopList,f)#dump the object to a file，存入对应的东西文件
f.close()
del shopList#remove shoplist
#read back from the storage
f=file(shopListFile)#取存储操作，这样的话，可以更有效
storedList=p.load(f)
print storedList
