class SchoolMember:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print 'Initialized school member:%s' %self.name#testting Chinese coding
		
        def tell(self):
		print 'Name:"%s" age:"%s"' % (self.name,self.age)

class Teacher(SchoolMember):
	def __init__(self, name,age,salary):
		SchoolMember.__init__(self,name,age)
		self.salary=salary
		print '(Initialized Teacher:%s)'%self.name
	def tell(self):
		#SchoolMember.tell(self)
		SchoolMember.tell(self)
		print 'Salary :%d'%self.salary
class Student(SchoolMember):
	def __init__(self,name,age,marks):
		SchoolMember.__init__(self,name,age)
		self.marks=marks 
		print '(InializedStudent:%s)'%self.name
	def tell(self):
		SchoolMember.tell(self)
		print 'Marks:"%d"' %self.marks
t=Teacher('Mrs.Shrividya',40,30000)
s=Student('Saroop',22,75)
print#prints a blank line
members=[t,s]
for member in members:
	member.tell()
