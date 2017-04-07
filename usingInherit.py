# -*- coding: utf-8 -*
#python注释，注意这个，utf-8编码是实现对应的功能。
class SchoolMember:
	def __init__(self,name,age):#attentionz第一次运行的时候，显示没有tell对象，但是，后来发现是自己
	#没有有效地对齐，这个要注意，全选拖着看到在于自己的对齐方式，没有统一，这个要注意，如何有效地进行对应
	#的标注
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
