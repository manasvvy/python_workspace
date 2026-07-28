'''
LAMBDA FUNCTION
-> its an anonymous function which is defined using lambda keyword
or
->its a function without a name, written in a single line and used  for short operations

NOTE-> LAMBDA KEYWORD IS USED
-> NO FUNCTION NAME
-> NO RETURN KEYWORD BV THE RESULT OF EXPRESSION IS AUTOMATICALLY RETURNED
-> MULTIPLE PARAMETERS ARE ALLOWED
-> ONLY 1 EXPRESSION IS ALLOWED

PURPOSE/IMPORTANCE OF THE LAMBDA FUNCTION : ITS BEST USED WHEN WE NEED TO PASS
A SIMPLE HELPER FUNCTION FOR A HIGHER ORDER FUNCTION 


*syntax:
variable=lambda parameters:expression

#calling the lambda, variable(argument)

*syntax2:
(lambda parameters:expression)(arguments)

'''
#using normal function

def add(a,b):
    return a+b
print(add(10,20))

print("---------------------------------------------")
#using lambda function

var= lambda a,b : a+b
print(var(10,20))

print("---------------------------------------------")

print((lambda a,b : a+b)(11,22))  #lambda function call in the same line

print("---------------------------------------------")

'''def square(n):                     #square is simple helper function/callbck function
    return n**2'''

#sq=lambda n : n**2 

'''def cube(n):
    return n**3'''

#cu=lambda n : n**3

def apply_op(fun,num):             #higher order function apply_op
    #print(num**2)
    print(fun(num))                #square(n)

'''sq=lambda n : n**2
cu=lambda n : n**3

we can directly write the lambda func exp in the func call'''

apply_op(lambda n : n**2,20)
apply_op(lambda n : n**3,30)

print("---------------------------------------------")

def is_even(n):
    return n%2==0
print(is_even(11))

print((lambda n : n%2==0)(7))

print("---------------------------------------------")

l=[10,20,30,40]
def square(n):
    return n**2

def hof(fun,coll):
    nl=[]
    for i in coll:
        sq=fun(i)
        nl.append(sq)
    return nl
print(hof(square,l))

print("------------------------------------")

print(hof(lambda n: n**2,l))
print(hof(lambda n: n**3,l))













