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
