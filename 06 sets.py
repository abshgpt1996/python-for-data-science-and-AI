Python 3.8.2 (v3.8.2:7b3ab5921f, Feb 24 2020, 17:52:18) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> S = {'a', 'b','c', 'a', 'd'}
>>> S
{'d', 'c', 'a', 'b'}
>>> #duplicate items were not present when the set was created.
>>> 
>>> #typecasting: convert list into set using set function.
>>> list = ['michael jackson', 'thriller', 'thriller',1982]
>>> set = set(list)
>>> set
{'thriller', 'michael jackson', 1982}
>>> ##set operations
>>> #addition
>>> set.add(NYC)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    set.add(NYC)
NameError: name 'NYC' is not defined
>>> set.add('NYC')
>>> set
{'thriller', 'NYC', 'michael jackson', 1982}
>>> # if we add the same item twice, there would be no effect as duplicates are not allowed in the set.
>>> #subraction
>>> set.remove('michael jackson')
>>> set
{'thriller', 'NYC', 1982}
>>> # we can verify if an element is in the set using in command.
>>> NYC in set
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    NYC in set
NameError: name 'NYC' is not defined
>>> 'NYC' in set
True
>>> 'player' in set
False
>>> 1982 in  set
True
>>> # we use ampersand(&) to find the intersection between the two sets.
>>> set2 = {'thriller','NYC', 'LA', 'CA'}
>>> set3 = set&set2
>>> set3
{'NYC', 'thriller'}
>>> #union of two sets
>>> set.union(set2)
{'CA', 'LA', 'NYC', 'thriller', 1982}
>>> set4 = set.union(set2)
>>> set4
{'CA', 'LA', 'NYC', 'thriller', 1982}
>>> #we can check if a set is subset using the issubset method.
>>> set2.issubset(set4)
True
>>> set3.issubset(set4)
True
>>> set2.issubset(set3)
False
>>> 