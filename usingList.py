shopList=['b','a']
print 'i have',len(shopList),'items to buy'
print 'these itmes are',
for i in shopList:
    print i, #check whether the comma is OK for the sighting
            #if not comma, a\nb,if comma, a \blank b,So,
            #the comma function should be used as the segmentaion
            #fenHao function used for getting the physical and logical lines
print '\ni also have to buy'
shopList.append('cNew')
print 'my shoplist now is',shopList
print 'i will sort it now'
shopList.sort()
print 'the first buying is ',shopList[0]#attention:use the [] to refer not ()
olditem=shopList[0]
del shopList[0]
print 'i bought the', olditem#why using the olditem to refer think deeper
print 'my shopping list is now',shopList
