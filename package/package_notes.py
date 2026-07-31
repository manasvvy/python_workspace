'''
IT IS A FOLDER THAT CAN HAVE MULTIPLE MODULE AND A SINGLE __init__.py FILE

NOTE: from py 3.3 version __init__.py file is not mandatory but still it is recommended

ADVANTAGES:
->it controls package level initilization
->also defines package level api
->it makes package level imports easier
->its helpful for package configuration(logging, package variable declaration)

*CMD TO RUN PY FILE INSIDE A PACKAGE :python -m packagename.modulename

init file executes when -> 1] a module of that package gets imported
                        -> 2] when executing the module of that package using the below cmd:
                              python -m packagename.modulename
                              
NOTE: __init__.py WILL BE EXECUTED FIRST IN THE PACKAGE WHEN ANY OF THE TWO CONDITIONS OCCUR

KEYWORDS:

1>import
->brings entire module into ur program
           syntax= import modulename1,mn2,mn3.....
-> to access or use the members inside a particular module we use
           syntax= modulename.membername

2>from
->used to print a specific variable , function or a class from the module
->by using ts we can avoid using the entire module name every now n then as a prefix
->use ts when u want clean readable code for frequently accessed members
           syntax1 = from modulename import module1,2,3....
           syntax2 = from packagename.modulename import membername

3>as
->used to give a shorter alt name to a member(var,func,classname)
           syntax1 = import modulename as m
           syntax2 = from modulename import membername1 as m1 , menbername2 as m2
'''

