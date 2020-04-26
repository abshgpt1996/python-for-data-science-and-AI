Python 3.8.2 (v3.8.2:7b3ab5921f, Feb 24 2020, 17:52:18) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> D = {'thriller': 1982,'back in the black': 1980}
>>> DICT[thriller]
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    DICT[thriller]
NameError: name 'DICT' is not defined
>>> D[thriller]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    D[thriller]
NameError: name 'thriller' is not defined
>>> D
{'thriller': 1982, 'back in the black': 1980}
>>> D['thriller']
1982
>>> DICT['thriller']
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    DICT['thriller']
NameError: name 'DICT' is not defined
>>> 
>>> 
>>> #we can also add value in the dictionary.
>>> D['graduation']=2007
>>> D
{'thriller': 1982, 'back in the black': 1980, 'graduation': 2007}
>>> #we can also delete the entry.
>>> del(D['thriller'])
>>> D
{'back in the black': 1980, 'graduation': 2007}
>>> #we can verify whether an element is in the dictionary using the in command.
>>> 'graduation' in D
True
>>> 'starboy' in D
False
>>> # we can also see all the keys in the dictionary.
>>> D.keys()
dict_keys(['back in the black', 'graduation'])
>>> # we can also obtain values.
>>> D.values()
dict_values([1980, 2007])
>>> 