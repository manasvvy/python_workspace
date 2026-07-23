
'''functions are treated as first class citizens in python: py treats a function 
->variables that can be stored
->as smthng that can be passed as an argument
->as smthng that can be returned from another function
->as smthng that can be around freely

1)function aliasing
->we can alias the function= assigning 1 functions reference into another variable name
->renaming an existing function

'''

def greet():
    print("gm chandu")
greet()               #fc using the existing function name
print("-------------------------------------------")
wish=greet            #function aliasing
wish()                #fc using new refrence name

print("-------------------------------------------")

#there is a func named add which takes 2 parameters and prints the sum of it, func alias it to combine

def add(a,b):
    print(a+b)
combine=add
combine(8,9)

print("-------------------------------------------")

'''2)passing a function as an arguments(higher order function)
->any function that accepts/returns another function as parameter that func is called as higher order function
'''
def eat():                 #callback
    print("eating")

def digest(fun):           #higher order function
    print(fun)
    fun()
print(eat)                 #address of eat function object
digest(eat)

print("-------------------------------------------")

#define a function name add takes 2 para, def a func named operations that accepts add func as a para, execute the operation func which should internally call the add func

def add(a,b):              #callback
    print(a+b)
    
def operations(fun):       #higher order function (function alias bc add=fun)
    fun(10,20)
operations(add)            #should only add function name

print("-------------------------------------------")

def add(a,b):              #callback
    print(a+b)
    
def operations(fun,n1,n2):       #higher order function (function alias bc add=fun)
    fun(n1,n2)
operations(add,80,20)            #should only add function name

print("-------------------------------------------")

'''3)returning an inner function = closures
->closure is going to happen when an inner function remembers the variable of outer function even after the outer function has completed its execution
or
->inner function that remembers and can access the variables from its enclosing function even after the execution
ie when a func returns another func it carries some data or logic with it, this itself is known as closure

//steps to create a closure//
1->create a outer func with variable
2->define an inner func which uses that variable
3->outer function returns an inner function activating the closure

*inner function can access and remember the global variable even after its destroyed
(ability to remember is closure)
=> closures are used in decorators and encapsulation logic'''

def outer():
    a=100           #enclosing variable
    def inner():
        print(a)    #outer function used in the inner function
    return inner    #ifc
inf=outer()         #ofc
#print(inf)
inf()               #we are able to access and remember the outer function variable even after its execution

print("-------------------------------------------")

#of name is get color and it has an enclosing var named as color blue inner function is show color showcase closure concepts

def get_color():
    color="blue"
    def show_color():
        print("color is",color)
    return show_color
b=get_color()
b()

print("-------------------------------------------")

#there is of named counter having enclosing variable count=0 there is if named increment and when its called the count variable should get incremented and print the count var achieve using closure

def counter():
    count=0
    def increment():
        nonlocal count
        count+=1
        print(count)
    return increment
k=counter()    
k()
k()
k()







































