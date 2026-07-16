'''
1=positional arguement -> passing the values in the same order as the parameters present in function
                       -> order matters
                       -> count matters (no of parameters should be equal to no of parameters)
                       ex- add'''

def register(name,age):
    print(f"{name} whose age is {age} registered successfully")
register("hari",12)

print("----------------------------------------------------------")

'''2=keyword arguments -> passing the value using the parameter names during the function call
                       -> order does not matter
                       -> cant pass the same argument more than once'''

def register(name,age):
    print(f"{name} whose age is {age} registered successfully")
register(age=12,name="hari")

print("----------------------------------------------------------")

def announce(winner,loser,goals,venue):
    print(f"{winner} scored {goals} goals and won against {loser} in {venue}")
announce(winner="argentina",loser="england",goals=2,venue="usa")

print("----------------------------------------------------------")


'''3=variable arguments -> these are passed in the function declaration when we dont know how many arguements will be passed during the function call.
                        
-> 3.1= variable positional arg -> *args in the function declaration (*variable can also be used) (packing)
                                -> collects the extra positional arguements into a TUPLE
                                -> only one *args should be used in function declaration
                                -> *args should come after all the positional parameters
                                
#NOTE: IF WE USE *collection IN THE FUNCTION CALL UNPACKING CAN BE OBSERVED
AND NO OF PARAMETERS SHOULD MATCH THE NO OF VALUES IN THE COLLECTION'''

def collect(*a): #function declaration
    print(a)
collect(10,20,30,55,26,4486,2558796,55645,58,9)

print("----------------------------------------------------------")

def collect(b,c,*a): #function declaration using *args (packing)
    print(b,c,a)
collect(10,20,30,55,26,4486,2558796,55645,58,9)

print("----------------------------------------------------------")

l=[11,22,33]
def extract(p,q,r):  #functiondeclaration
    print(p,q,r)     #functionbody
extract(*l)          #using *collection in fc (unpacking)

print("----------------------------------------------------------")

def combine(*args):    #packing bc *args in function declaration
    print(args)
    
l=[12,13,14,15,16,17]    
combine(*l)            #unpacking bc *collection in function call

print("----------------------------------------------------------")


'''-> 3.2= variable keyword arg -> **kwargs in the function declaration
                                -> collects exxtra keyword arguments into a dict
                                -> only one **kwargs should be used in function declaration
                                -> **kwargs should be used after all types of parameters
                                -> keywords arguments not matching the parameter name is also accepted in the dictionary'''

def collect(**kwargs):                  #**kwargs in function declaration
    print(kwargs)
collect(name="messi",age=39,goals=7)    # variable no of keywords arguments


'''4=default arguements

'''                       


