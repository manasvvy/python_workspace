
'''ITERATOR
1-> object in python that allows to traverse/iterate to all the elements of a collection . one element at a time
2-> iterator is unidirectional(allows to travers left to right)
3-> it allows partial iteration

THERE ARE 2 MAIN FUNCTIONS

1. iter(collection)
-> its a predefined function that takes collection as parameter and returns an iterator object
->iterator object keeps a cursor that moves to the next element  every time next() is called

2. next(iterator)
-> predefined func that takes the iterable object and returns the next element from the iterator and advances (moves)
the cursor
->when no elements are left in the iterator it raises stopiteration

NOTE= ITERABLE IS EXHAUSTIBLE (ONLY ONCE WE CAN ITERATE THRU IT)
=>iterator logic is used in for loops
'''

#step 1=create or define an iterator using
l=[10,20,30,40]     

itr_obj=iter(l)     #returns an iterator object
print(itr_obj)      #list_iterator object

#step 2=call next() by passing itr_obj within it
'''print(next(itr_obj))
print(next(itr_obj))
print(next(itr_obj))
print(next(itr_obj))'''

print("-----------------------------------------------")

#one way to iterate/traverse an iterator is using next()
#2nd way to traverse an iterator is using for loop
#3rd way to obtain the iterator element is using explicit typecasting

'''for i in itr_obj:    #unable to see the elements bc its alr exhausted
    print(i)'''

print("-----------------------------------------------")

'''print(tuple(itr_obj)) #explicit typecasting'''   

i=0
while i < len(l):
    print(next(itr_obj))
    i=i+1





















