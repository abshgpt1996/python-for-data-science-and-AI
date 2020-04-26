Python 3.8.2 (v3.8.2:7b3ab5921f, Feb 24 2020, 17:52:18) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> tuple1 = ('disco',1,1.0)
>>> type(tuple1)
<class 'tuple'>
>>> tuple1[0]
'disco'
>>> tuple1[1]
1
>>> tuple1[2]
1.0
>>> tuple1[-3]
'disco'
>>> tuple1[-2]
1
>>> tuple1[-1]
1.0
>>> # An index of -1 corresponds to the last index of the tuple.
>>> ## we can concatenate and combine tuples by adding them.
>>> tuple2 = tuple1 + ('hard rock', 10)
>>> tuple2
('disco', 1, 1.0, 'hard rock', 10)
>>> 
>>> #slicing
>>> tuple2[0:2]
('disco', 1)
>>> tuple2[1:3]
(1, 1.0)
>>> tuple2[3:5]
('hard rock', 10)
>>> 
>>> #length of tuple
>>> len(tuple1)
3
>>> len(tuple2)
5
>>> #tuples are immutables i.e. we cannot change them.
>>> tuple3 = sorted(tuple2)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    tuple3 = sorted(tuple2)
TypeError: '<' not supported between instances of 'int' and 'str'
>>> # a tuple can contain other tuple as well. this is called nesting.
>>> NT = (1,2,('pop','rock'),(3,4),('disco', (1,2)))
>>> NT[2]
('pop', 'rock')
>>> NT[5]
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    NT[5]
IndexError: tuple index out of range
>>> NT[4]
('disco', (1, 2))
>>> NT[2][1]
'rock'
>>> NT[4][2]
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    NT[4][2]
IndexError: tuple index out of range
>>> NT[4][1][1]
2
>>> 