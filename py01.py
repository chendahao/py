# print('hello world')
# name=input()
# a=100
# if a>100:
# 	print(a)
# else:
# 	print(-a)

# a=10/3
# b=int(a)
# print(a)
# print(b)

# def myabs(a):
# 	try:
# 		int(a)
# 	except Exception as e:
# 		raise
# 	else:
# 		pass
# 	finally:
# 		pass
# 	if a>=0:
# 		return a
# 	else:
# 		return -a
# print(myabs(3))

# def power(x,n):
# 	s=1
# 	while n>0:
# 		n=n-1
# 		s=s*x
# 	return s
# print(power(3,3))


#递归调用
# def fact(n):
# 	if n==1:
# 		return 1
# 	return n*fact(n-1)
# print(fact(4))

# l=list(range(100))

# print(l[:10])
# print(l[-3:])

# d={'a':1,'b':2,'c':3}
# for k,v in enumerate(d):
# 	print(k)
# 	print(v)

# list(range(1,10))
# print([x*x for x in range(1,11)])
#---————————————————————
# import  os
# print([d for d in os.listdir(',')])
#---————————————————————

# std1={'name':'m','score':90}
# std2={'name':'n','score':91}
# def printscore(std):
# 	print('%s:%s' % (std['name'],std['score']))

# printscore(std1)
# printscore(std2)

class Student(object):
	"""docstring for Student"""
	def __init__(self, name , score):
		super(Student, self).__init__()
		self.__name = name
		self.__score = score
	def printscore(self):
		print('%s:%s' % (self.__name,self.__score))
	def getgrade(self):
		if self.__score>=90:
			return 'A'
		elif self.__score>=60:
			return 'B'
		else:
			return 'C'
	def getname(self):
		return self.__name
	def getscore(self):
		return self.__score		
bart=Student('Bart',59)
lisa=Student('lisa',60)
bart.printscore()
# print(lisa.getname(),lisa.getgrade())     //虽然双下划线的变量为私有变量（__）但是可以通过_类型__变量（_Student__name）
print(lisa._Student__name,lisa.getgrade())

