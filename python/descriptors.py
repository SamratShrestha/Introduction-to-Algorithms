class RevealAccess(object):
    def __init__(self,initval=None,name="var"):
        self.val = initval
        self.name = name

    def __get__(self,obj,objtype):
        print("getting",self.name)
        return self.val

    def __set__(self,obj,val):
        print("setting",self.name)
        self.val = val

    def __delete__(self,obj):
        print("deleting",self.name)


class MyClass(object):
    x = RevealAccess(10,'var"x"')
    y = 10


m = MyClass()
print(m.x)

m.x = 100
print(m.x)

del m.x


class InitOnAccess:
    def __init__(self,init_func,*args,**kwargs):
        self.klass = init_func
        self.args = args
        self.kwargs = kwargs
        self._initialized = None

    def __get__(self,instance,owner):
        if self._initialized is None:
            print('initialzied')
            self._initialized = self.klass(*self.args,**self.kwargs)
        else:
            print('cached')
        return self._initialized

import random
class WithRandomAccess:
    lazily_sorted = InitOnAccess(sorted,[random.random() for _ in range(10)])

m = WithRandomAccess()
print(m.lazily_sorted)
print(m.lazily_sorted)

class lazy_property:
    def __init__(self,function):
        self.fget = function

    def __get__(self,obj,cls):
        value = self.fget(obj)
        setattr(obj,self.fget.__name__,value)
        return value

class WithLazyProperty:
    @lazy_property
    def lazily_initialized(self):
        return sorted([[random.random() for _ in range(4)]])

t = WithLazyProperty()
print(t.lazily_initialized)

class UserAccount:
    def __init__(self,username,password):
        self.username = username
        self._password = password

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self,value):
        self._password = password

