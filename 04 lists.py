Python 3.8.2 (v3.8.2:7b3ab5921f, Feb 24 2020, 17:52:18) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> L = ['Michael Jackson', 10.1, 1982]
>>> L
['Michael Jackson', 10.1, 1982]
>>> L = L + [[1,2], ('A', 1)]
>>> L
['Michael Jackson', 10.1, 1982, [1, 2], ('A', 1)]
>>> # lists are mutable
>>> L[2]
1982
>>> L[3]
[1, 2]
>>> L[3][1]
2
>>> L[4][0]
'A'
>>> L[4][1]
1
>>> L[-5]
'Michael Jackson'
>>> L[-3]
1982
>>> #SLICING
>>> L[3:5]
[[1, 2], ('A', 1)]
>>> L[0:1]
['Michael Jackson']
>>> L[0:3]
['Michael Jackson', 10.1, 1982]
>>> L.extend(['pop', 10])
>>> l
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    l
NameError: name 'l' is not defined
>>> L
['Michael Jackson', 10.1, 1982, [1, 2], ('A', 1), 'pop', 10]
>>> #extending the list
>>> #appendinh the list. i.e. adding one element to the list.
>>> L.append(['rock', 3])
>>> L
['Michael Jackson', 10.1, 1982, [1, 2], ('A', 1), 'pop', 10, ['rock', 3]]
>>> L[0] = 'Rohit Sharma'
>>> L
['Rohit Sharma', 10.1, 1982, [1, 2], ('A', 1), 'pop', 10, ['rock', 3]]
>>> #changing the element of the list.
>>> 
>>> #deleting an element of the lsit.
>>> del(L[0])
>>> L
[10.1, 1982, [1, 2], ('A', 1), 'pop', 10, ['rock', 3]]
>>> 
>>> 
>>> #we can convert a string to list using split.
>>> 'hard rock'.split()
['hard', 'rock']
>>> # split method converts every group of characters separated by space into an element of a list.
>>> 
>>> 'A,B,C,D'.split(',')
['A', 'B', 'C', 'D']
>>> #We can use the split function to separate strings on a specific character known as a delimiter.We simply pass the delimiter we would like to split on as an argument: in this case, a comma.
>>> 
>>> # multiple names referring to the same object is known as aliasing.
>>> #when we set one variable M equal to L, then they are referring to the same list.
>>> M=L
>>> M
[10.1, 1982, [1, 2], ('A', 1), 'pop', 10, ['rock', 3]]
>>> #if we change the value of L, then the value of M will also change as both are referencing the same list.
>>> L[0]
10.1
>>> M[0]
10.1
>>> L[0]=5
>>> L
[5, 1982, [1, 2], ('A', 1), 'pop', 10, ['rock', 3]]
>>> M
[5, 1982, [1, 2], ('A', 1), 'pop', 10, ['rock', 3]]
>>> # we can also clone list by using following syntax.
>>> N=L[:]
>>> # here variable L references one list. variable N references new copy of the original list.
>>> N
[5, 1982, [1, 2], ('A', 1), 'pop', 10, ['rock', 3]]
>>> L
[5, 1982, [1, 2], ('A', 1), 'pop', 10, ['rock', 3]]
>>> L[0]= 50
>>> L
[50, 1982, [1, 2], ('A', 1), 'pop', 10, ['rock', 3]]
>>> N
[5, 1982, [1, 2], ('A', 1), 'pop', 10, ['rock', 3]]
>>> #help command
>>> help(L)
Help on list object:

class list(object)
 |  list(iterable=(), /)
 |  
 |  Built-in mutable sequence.
 |  
 |  If no argument is given, the constructor creates a new empty list.
 |  The argument must be an iterable if specified.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iadd__(self, value, /)
 |      Implement self+=value.
 |  
 |  __imul__(self, value, /)
 |      Implement self*=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(self, /)
 |      Return a reverse iterator over the list.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(self, /)
 |      Return the size of the list in memory, in bytes.
 |  
 |  append(self, object, /)
 |      Append object to the end of the list.
 |  
 |  clear(self, /)
 |      Remove all items from list.
 |  
 |  copy(self, /)
 |      Return a shallow copy of the list.
 |  
 |  count(self, value, /)
 |      Return number of occurrences of value.
 |  
 |  extend(self, iterable, /)
 |      Extend list by appending elements from the iterable.
 |  
 |  index(self, value, start=0, stop=9223372036854775807, /)
 |      Return first index of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  insert(self, index, object, /)
 |      Insert object before index.
 |  
 |  pop(self, index=-1, /)
 |      Remove and return item at index (default last).
 |      
 |      Raises IndexError if list is empty or index is out of range.
 |  
 |  remove(self, value, /)
 |      Remove first occurrence of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  reverse(self, /)
 |      Reverse *IN PLACE*.
 |  
 |  sort(self, /, *, key=None, reverse=False)
 |      Sort the list in ascending order and return None.
 |      
 |      The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
 |      order of two equal elements is maintained).
 |      
 |      If a key function is given, apply it once to each list item and sort them,
 |      ascending or descending, according to their function values.
 |      
 |      The reverse flag can be set to sort in descending order.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

>>> 