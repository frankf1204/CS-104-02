Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> print ("Hello World")
Hello World
>>> name= "Frank"
>>> print(name)
Frank
>>> print ("Hello"+name)
HelloFrank
>>> a=2
>>> print ("Hello "+a)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print ("Hello "+a)
TypeError: can only concatenate str (not "int") to str
>>> type(name)
<class 'str'>
>>> type(a)
<class 'int'>
>>> a=2.0
>>> type(a)
<class 'float'>
>>> a=2.5
>>> a="abc"
>>> print name
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(name)?
>>> print name
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(name)?
>>> print (name)
Frank
>>> type(a)
<class 'str'>
>>> a=2
>>> b=3
>>> c=a+b
>>> print(c)
5
>>> type(c)
<class 'int'>
>>> a=2.0
>>> b=3
>>> c=a+b
>>> print(c)
5.0
>>> type(c)
<class 'float'>
>>> c=int (a+b)
>>> print(c)
5
>>> type(c)
<class 'int'>
>>> a="2"
>>> b=3
>>> c=a+b
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    c=a+b
TypeError: can only concatenate str (not "int") to str
>>> type(a)
<class 'str'>
>>> c=int(a)+b
>>> print(c)
5
>>> type(a)
<class 'str'>
>>> a = int(a)
>>> type(a)
<class 'int'>
>>> a="x"
>>> int(a)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    int(a)
ValueError: invalid literal for int() with base 10: 'x'
>>> a=2.6
>>> a=int(a)
>>> a+"2.6"
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    a+"2.6"
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> a=float(a)
>>> print(a)
2.0
>>> type(a)
<class 'float'>
>>> a=False
>>> print(a)
False
>>> numberOfScores = input("Please enter the number of scores you want to average: ")
Please enter the number of scores you want to average: 