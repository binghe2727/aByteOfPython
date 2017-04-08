class Person:
    population=0

    def __init__(self,name):
        self.name=name
        print 'Initialize %s' %self.name#attention:not ,comma between
        Person.population+=1#use the Person. to refer the object
    def __del__(self):
        print '%s say bye' %self.name
        Person.population-=1
        if Person.population==0:
            print 'i am the last one'
        else:
            print 'there are also %d persons in it' %Person.population
    def sayHi(self):
        print 'my name is %s' %self.name
    def howMany(self):
        if Person.population==1:
            print 'i am the last one'
        else:
            print 'i am not the lat one,the %d persons here' %Person.population

aa=Person('aa')
aa.sayHi()
aa.howMany()
bb=Person('bb')
bb.sayHi()
bb.howMany()
bb.__del__()#atttention:use this format type to refer the method using of __bb__(),pay attention
aa.sayHi()
aa.howMany()



    
    
