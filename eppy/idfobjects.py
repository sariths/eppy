"""subclass from collections.MutableSequence to get finer ontrol over a list like object. 

this is to work with issue 40 in github:

idf1.idfobjects['BUILDING'] is a list and is not connected to idf1.model.dt['BUILDING']
list has to be subclassed to solve this problem
"""

# Alex Marelli describes how to use collections.MutableSequence in
# <http://stackoverflow.com/questions/3487434/overriding-append-method-after-inheriting-from-a-python-list>
# Here I recreate and test his example

import collections

class TypedList(collections.MutableSequence):

    def __init__(self, oktypes, *args):
        self.oktypes = oktypes
        self.list = list()
        self.extend(list(args))

    def check(self, v):
        if not isinstance(v, self.oktypes):
            raise TypeError, v

    def __len__(self): return len(self.list)

    def __getitem__(self, i): return self.list[i]

    def __delitem__(self, i): del self.list[i]

    def __setitem__(self, i, v):
        self.check(v)
        self.list[i] = v

    def insert(self, i, v):
        self.check(v)
        self.list.insert(i, v)

    def __str__(self):
        return str(self.list)
        
        
x = TypedList((str, unicode), 'foo', 'bar')
x.append('zap')
print x
# x.append(23)
x.extend(['a', 3, 'b', 'c'])       
print x