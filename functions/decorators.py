'''DECORATORS-it is a function that modifies the beaviour of another function without changing its code
or
it is a func that takes another func as input adds extra behaviour and returns a new function without changing the original function code
STEPS TO DEFINE A DECORATORS
1)create a nested funcction wherein the outer function must have only 1 parameter that takes another function(function to de decorated)
2)the inner function should contain the decorators logic within it(extra implementation)
3)the outer func should return the address of the inner func
outer function name=decorator, inner function name=wrapper
'''

def decorator(fun):                 #decorator taking 1 para
    def wrapper():                  #wrapper containing decorators logic
        print("choose the bubble wrap")
        fun()                       #gift
        print("pack the gift")
    return wrapper
def gift():                         #function to be decorated
    print("barbie is the gift")
gift=decorator(gift)    
gift()



    
