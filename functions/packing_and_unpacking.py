#packing=1)process of collecting/looping multiple value into a single variable
        #2)py auto packs values into tuple
#1.1* manual packing
#1.2* implicit packing
""" 1.1 the user explicitly decides the datatype/collection and manually packs the values using []. (), {}
    1.2 when we have multiple comma seperated values assigned to a single variable and its grouped or collected into TUPLE by default"""

a=10,20,True,5j,30.1,"m" #can pack any datatype as long as its seperated by ,
print(a)
print(type(a))

print("-------------------------------------")

#unpacking=1) the process of extracting, retrieving values from a sequence and assigning em to the individual variable
          #2) no of variable should match the no of values in the sequence during unpacking unless we use * for leftovers

"""2.2 extended iterable unpacking when we dont know how many values to unpack, we use *variablename , which collects the remaining value as a list
   2.3 only 1 * is used
   2.4 *variablename can be used as the start middle or end

l=[10,20,30,40] #4values
     
a,b,c,d=l
print(a,b,c,d)

l=[10,20,30,40,85,2552,67,77,99,54,320,326,3454,4653] #4values
     
a,b,c,*d=l #extended iterable unpacking
print(a,b,c)
print(d)

*a,b,c,d=l #extended iterable unpacking
print(b,c,d)
print(a)

a,b,*c,d=l #extended iterable unpacking
print(a,b,d)
print(c)"""


d={1:10,2:20,3:30,4:40}
a,b,*c,d=d #extended iterable unpacking
print(a)
print(b)
print(c)
print(d)

d="RCSKB"
a,*b,c,=d #extended iterable unpacking
print(a)
print(b)
print(c)
print(d)

















