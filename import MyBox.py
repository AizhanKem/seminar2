from mybox import Mybox
from myboxiterator import MyBoxIterator
from myclass import MyClass
b=MyBox()
b.add(MyClass('Symbat', 'Karaganda', 'Teacher'))
b.add(MyClass('Den', 'Moskva', 'Driver'))
b.add(MyClass('Zere', 'Almaty', 'Student'))

b.remove(1)
for i in b:
	i.meth_1()