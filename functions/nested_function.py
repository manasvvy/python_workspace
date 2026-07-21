'''nested functions are used to organise the logic and group/reuse small tasks that relevant only inside the outer function
-> it acts like a helper function but which is kept private within the outer function
NOTE-THE INNER FUNCTION SHOULD BE CALLED WITHIN THE OUTER FUNCTION UNLESS IT IS RETURNED
1*GLOBAL VARIABLE CAN BE ACCESSED INSIDE THE OUTER AND INNER FUNCTION
2*ENCLOSING VARIABLES ARE THE VARIABLES OF THE OUTER FUNCTION WHICH ARE ACCESSED INSIDE THE INNER FUNCTION
->if we dont access such variables inside the inner function, it wont be considered as enclosing variables
->if we try to modify the ev inside the inner function we get unboundlocalerror hence we use the keyword "nonlocal" inside the inner function'''

def outer():                                #outer function declaration
    print("inside outer function")          #outer function body
    def inner():                            #inner function declaration
        print("inside the inner function")  #outer function call
    inner()
outer()
print("-----------------------------------------")


a=100                                         #global variable
def outer():                                  #outer function declaration
    print("inside outer function",a)          #outer function body
    def inner():                              #inner function declaration
        print("inside the inner function",a)  #outer function call
    inner()
outer()
print("-----------------------------------------")

a=100                                           #global variable
def outer():                                    #outer function declaration
    b=200                                       #enclosing variable
    print("inside outer function",a,b)          #outer function body
    def inner():                                #inner function declaration
        c=300                                   #local variable
        print("inside the inner function",a,b,c)  #outer function call
    inner()
outer()
print("-----------------------------------------")

def outer():                                  #outer function declaration
    b=200                                     #ev
    b+=25
    print("modified b inside the outer function",b)
    def inner():                              #inner function declaration
        nonlocal b                            #modifies b
        b-=25
        print("print inner function",b)       #outer function call
    inner()
outer()
print("-----------------------------------------")

#define a nested function where counter is the outer function name and nested function name is increment , define an ev named as count initialize to 0, invoke the increment 3 times and print the count value each time u call the increment function

def counter():
    count=0
    def increment():
        nonlocal count
        count+=1
        print("count",count)
    increment()
    increment()
    increment()
counter()    

print("-----------------------------------------")














