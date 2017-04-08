class Person:
    def __init__(self,name):
        self.name=name#attention:included to create a new field(variable in python unlike java
        #pay more attention to it.)
    def sayHi(self):
        print 'name is',self.name
p=Person('Sam')#attention, first time, i use sam not'sam',not defined, pay more attention
    #to this error for further debugging,!!!remember to understand the variables and paramters
#in python, use the string function to avoid the error
p.sayHi()
