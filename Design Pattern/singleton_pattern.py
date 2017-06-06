

class OnlyOne():
	class __OnlyOne():
		def __init__(self, arg):
			self.val = arg
		def __str__(self):
			return repr(self)+self.val

	instance = None
	def __init__(self, arg):
		if not OnlyOne.instance:
			OnlyOne.instance = OnlyOne.__OnlyOne(arg)
		else:
			OnlyOne.instance.val = arg

	def __getattr__(self, name):
		return getattr(self.instance, name)


x= OnlyOne('sausage')
print 'x=',x

y = OnlyOne('eggs')
print 'y=',y

z = OnlyOne('spam')
print z

print 'x=',x
print 'y=',y


#Singleton with closures, dict

def singleton(cls):
	instances = {}

	def get_instance():
		if cls not in instances:
			instances[cls] = cls()
		return instances[cls]

	return get_instance

#@singleton    #:simpler way to define without set Counter = singleton(Counter)
class Counter():
	def __init__(self):
		self.count =1

	def inc(self):
		self.count += 1

print type(Counter)

Counter = singleton(Counter)

print type(Counter)


print Counter()
print Counter()

