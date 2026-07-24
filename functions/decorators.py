'''DECORATORS-it is a function that modifies the beaviour of another function without changing its code
or
it is a func that takes another func as input adds extra behaviour and returns a new function without changing the original function code
STEPS TO DEFINE A DECORATORS
1)create a nested funcction wherein the outer function must have only 1 parameter that takes another function(function to de decorated)
2)the inner function should contain the decorators logic within it(extra implementation)
3)the outer func should return the address of the inner func
outer function name=decorator, inner function name=wrapper
'''
#CONCEPTS USED IN THE DECORATORS
#function
#para and arguments
#nested function
#packing unpacking
#function aliasing
#higher order function
#closure

'''USES OF DECORATORS
1. CODE REUSABILITY=> function can be reused multiple time w/o affecting the other logic
2. SEPERATION OF CONCERNS=> decorators helps us seperate what a function does from how and when it is execute
3. USEFUL FOR CROSSCUTTING CONCERNS=> certain behaviours apply across many parts of an applications such as:
=logging
=authentication
=error handling
=performance monitoring'''


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

print("----------------------------------------------------------------")

def decorator(cake):                                #decorator taking 1 para
    def wrapper():                                  #wrapper containing decorators logic
        print("choose the flavor of the cake")
        cake()                                      #calling function is mandatory
        print("pack the cake")
    return wrapper                                  #returning wrapper is mandatory
def bake_cake():                                    #function to be decorated
    print("bake this cake")
bake_cake=decorator(bake_cake)                      #decorator should have atleast 1 para() which should be another function
bake_cake()                                         #wrapper internally and bake cake is extarnal

print("----------------------------------------------------------------")

'''NOTE=> IF U WANNA PASS PARAMETER TO THE FUNCTION TO BE DECORATED
1. FUNCTION TO BE DECORATED AND WRAPPER FUNCTION SHOULD HAVE EXACTLY SAME NO OF PARAMETER AND NAMES
2. FIND THAT PARAMETER MUST BE USED IN THE ORIGINAL FUNCTION CALL
3. WHEN CALLING THE DECORATOR FUNCTION PASS THE CORRECT NO OF ARGUMENTS AS PER PARAMETER
'''

def decorator(cake):                                #decorator taking 1 para
    def wrapper(*args):                                  #wrapper containing decorators logic
        print("choose the flavour of the cake")
        cake(*args)                                      #calling function is mandatory
        print("pack the cake")
    return wrapper                                  #returning wrapper is mandatory
def bake_cake(*args):                                    #function to be decorated
    print("baked this cake", args)
bake_cake=decorator(bake_cake)                      #decorator should have atleast 1 para() which should be another function
bake_cake("egg","flour","baking soda","cocoa powder") #wrapper internally and bake cake is extarnal

print("----------------------------------------------------------------")

def decorator(cake):                                #decorator taking 1 para
    def wrapper(*args,**kwargs):                                  #wrapper containing decorators logic
        print("choose the flavour of the cake")
        cake(*args,**kwargs)                                      #calling function is mandatory
        print("pack the cake")
    return wrapper                                  #returning wrapper is mandatory
def bake_cake(*args,**kwargs):                                    #function to be decorated
    print("baked this cake", args,kwargs)
bake_cake=decorator(bake_cake)                      #decorator should have atleast 1 para() which should be another function
bake_cake("egg","flour","baking soda","cocoa powder",milk="toned milk",essence="vanilla")                                         #wrapper internally and bake cake is extarnal

print("----------------------------------------------------------------")

def decorator(cake):                                
    def wrapper(*args,**kwargs):                    #packing in fd                                
        print("choose the flavour of the cake")
        cake(*args,**kwargs)                        #unpacking in fc              
        print("pack the cake")
    return wrapper                                  #packing in fd

@decorator                                          #@ automatically calls decorator 
def bake_cake(*args,**kwargs):                                  
    print("baked this cake", args,kwargs)
#bake_cake=decorator(bake_cake)                     #manual decoration           
bake_cake("egg","flour","baking soda","cocoa powder",milk="toned milk",essence="vanilla")#wrapper internally and bake cake is extarnal

