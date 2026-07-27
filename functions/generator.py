'''generator is an object in python
->it is a function used to create a sequence of elements using the YIELD keyword
->if a user defined funcc contains atleast 1 yeild keywords then the func becomes generator
->a generator generates values one by one not at once
->its focused mostly on creating custom sequences(odd even prime no etc)

steps to create
=>created only once when the function containing yield keyword is called
=>each yeild u used returns one value when 'next()' function is called or 'for loop' asks for it

NOTE YIELD
- KEYWORD TO CREATE GENERATOR
- IT RETURNS THE YEILDED VAL TO FUNCCALLER
- IT PAUSES THE FUNCTION (REMEMBERS VARIABLE AND GOES TO NEXT LINE)
- WHEN WE CALL NEX() AGAIN, IT RESUMES RIGHT AFTER THE YEILD
- AUTOMATICALLY CREATES AN ITERATOR
- GENERATOR IS AN ITERATOR


'''

#step1 define a func with atleast 1 yeild keyword

'''def display():          #generator function
    value=1
    yield 1**2
    value+=2
    yield value**2
    value+=3
    yield value**2
    value+=4
    yield value**2'''

def display():
    for i in range(1,6):
        yield i**2+1

    
#step2 call the generator function to create generator
    
gen_obj=display()       #assign the generator to create a variable    

#step3 call next() by passing generator obj as parameter

'''print(next(gen_obj))
print(next(gen_obj))    #u can print unrelated things in between these
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))'''

#print(list(gen_obj))    #explicit typecasting of generator object

for i in gen_obj:
    print(i)             #generator can be used w for loop

















