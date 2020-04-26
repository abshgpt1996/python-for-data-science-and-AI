Python 3.8.2 (v3.8.2:7b3ab5921f, Feb 24 2020, 17:52:18) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> name = "Michael jackson"
>>> name[0]
'M'
>>> name[12]
's'
>>> name[-5]
'c'
>>> #negative indexing can also be used.
>>> #negative indexing starts from the right hand side which is -1. positive indexing starts from LHS and starts from 0.
>>> 
>>> ##slicing
>>> name[0:4]
'Mich'
>>> name[5:8]
'el '
>>> ##stride
>>> name[::2]
'Mcaljcsn'
>>> #stride gives every second value.
>>> name[0:5:2]
'Mca'
>>> name[0:9:2]
'Mcalj'
>>> #length function to obtain the length of the string.
>>> len(name)
15
>>> len("abhishek")
8
>>> statement = name + "is the best"
>>> statement
'Michael jacksonis the best'
>>> #tuples
>>> 3*name
'Michael jacksonMichael jacksonMichael jackson'
>>> 3* "abhishek"
'abhishekabhishekabhishek'
>>> 3*" abhishek"
' abhishek abhishek abhishek'
>>> 
>>> #immutable
>>> #you cannot change the value of the string but you can create a new string.
>>> 
>>> #back slashes represent the beginning of escape consequences. escape sequences are strings that are difficult to input.
>>> ## /n represnts the new line.
>>> print("abhishek /n is the best")
abhishek /n is the best
>>>  print("abhishek/n is the best")
 
SyntaxError: unexpected indent
>>>  print("abhishek\n is the best")
 
SyntaxError: unexpected indent
>>> 
>>> 

>>> 
>>> 
>>> 

>>> 
>>> 
>>> 
>>> print("abhishek\n is the best")
abhishek
 is the best
>>> # \t represnts the tab.
>>> print("abhishek\tgupta")
abhishek	gupta
>>> #\\
>>> print("abhishek\\gupt")
abhishek\gupt
>>> 
>>> 
>>> #string methods
>>> a = "thriller is great"
>>> b = a.upper()
>>> b
'THRILLER IS GREAT'
>>> 
>>> #replace function
>>> a="virat is the best"
>>> b=a.replace(virat,rohit)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    b=a.replace(virat,rohit)
NameError: name 'virat' is not defined
>>> b=a.replace("virat","rohit")
>>> b
'rohit is the best'
>>> 
>>> #find
>>> name.find('el')
5
>>> name.find('jack')
8
>>> #if the substring is not in the string, the output is -1.
>>> name.find("r")
-1
>>> 