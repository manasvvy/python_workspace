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

print("------------------------------------")

print(hof(lambda n: n**3,l))

print("--------------map object----------------")

#PREDEFINED HIGHER ORDER FUNCTIONS
'''
1->MAP
map(function,iterable)
    function= should take 1 argument
    iterable= sequence like list, tuple
=>MAP APPLIES THE GIVEN FUNCTION TO EACH ELEMENT OF THE ITERABLE
=>MAP RETURNS A MAP OBJECT(AN ITERABLE)'''

print(list(map(lambda n:n**2,l)))

print("--------------filter object----------------")


'''2->FILTER
filter(function,iterable)
        function= should take 1 value only and return bool val
        iterable= sequence
=>FILTER FUNCTION FILTERS OUT THE ELE FROM AN ITERABLE BASED ON THE HOF
=>IT RETURNS ONLY THOSE ELEMENT WHERE FUNCTION RETURNS TRUE '''

print(list(filter(lambda n:n%2==0,[1,2,3,4,5,6,7,8,9])))

print("--------------reduce object----------------")

'''
3->REDUCE
reduce(function,iterable)
        function= should take 2 parameters and return single value
        iterable= sequence
=> IT IS A FUNCTION FRROM FUNCTOOL MODULE
=>IT APPLIES A GIVEN FUNCTION ONE AFTER ANOTHER TO THE ITEMS OF AN ITERABLE
THEREBY REDUCING THEM TO A SINGLE VALUE

NOTE=>FROM FUNCTOOLS IMPORT REDUCE -> IMPORT THE FUNCTION

'''
from functools import reduce

#add
l=[10,20,30,40,50,60,70,80,90]
print(reduce(lambda a,b:a+b,l))

#multiply
l=[1,2,3,4,5,6,7,8,9]
print(reduce(lambda a,b:a*b,l))

#even nos square sequence
l=[2,3,4,6,11,13,14]
print(list(map(lambda n:n**2,filter(lambda n:n%2==0,l))))










