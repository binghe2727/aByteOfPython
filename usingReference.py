#!/usr/bin/python
# Filename: reference.py
print 'Simple Assignment'
shoplist = ['apple', 'mango', 'carrot', 'banana']
mylist = shoplist # mylist is just another name pointing to the same object!
                            #like the java reference get;
    #attention: the uses of the value changing linking, should be focused and warned.
del shoplist[0]
print 'shoplist is', shoplist
print 'mylist is', mylist
# notice that both shoplist and mylist both print the same list without
# the 'apple' confirming that they point to the same object
print 'Copy by making a full slice'
mylist = shoplist[:] # make a copy by doing a full slice
#attention this chaning to avoid the changes of the time like the
#java similar to use the array element to finish the transimission of data
del mylist[0] # remove first item
print 'shoplist is', shoplist
print 'mylist is', mylist
# notice that now the two lists are different
