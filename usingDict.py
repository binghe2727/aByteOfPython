#using the dict data structure
ab={
    'a':'place1',
    'b':'place2',
    'c':'place3'
    }
print 'a place is %s' % ab['a']#attention: using the 'a' not a to refer the object;keep the same pointing!
#add new
ab['dNew']='place4'
#delete
del ab['a']
print '\n there are %d items in the \n' %len(ab)#attention:there is no comma before %ab/%len(ab)
for name, address in ab.items():
    print 'the %s at %s'  %(name,address)#name,address can be changed like into name1,address1,
                                                                #the name character is not specified,attention!!

if 'b'in ab:#or ab.has_key('b')$in ab.items() is also ok for the function
    print '\n b address is %s',ab['b']    
