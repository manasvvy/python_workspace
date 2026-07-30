''' 
COMPREHENSIONS WERE INTRODUCED TO REPLACE THE LOOP+APPEND PATTERN IN A READABLE AND DECLARATIVE WAY
=>it is a compact,readable 1 line way to create a new collection
=>it combines 3 operations:
iteration + transformation + filtering

THERE ARE 3 TYPES OF COMPREHENSIONS:'''

'''1-> LIST COMPREHENSION
syntax1:
[expression for variable in sequence]'''
#square of each ele
l=[2,4,6,11,13,14]
nl=[i**2 for i in l]
print(nl)

#increase every element
l=[2,4,6,11,13,14]
nl=[i+10 for i in l]
print(nl)

#convert and create a new list
ln=['karna','varna','marna']
nl=[i.upper() for i in ln]
print(nl)

'''syntax2:
[true_expression for variable in sequence if condition]'''

#square even no and odd no
l1=[2,4,6,11,13,14]
nl1=[i**2 for i in l if i%2==0] #even
nl2=[i**2 for i in l if i%2!=0] #odd
print(nl1)
print(nl2)

'''syntax3:
[true_expression if condition else false_expression for variable in sequence]'''

ll=[2,4,6,11,13,14]
nll=[i**2 if i%2==0 else i**3 for i in ll]
print(nll)

'''2-> SET COMPREHENSION
syntax1:
{expression for variable in sequence}
'''
ln={'karna','varna','marna'}
nl={i.upper() for i in ln}
print(nl)

'''syntax2:
{true_expression for variable in sequence if condition}'''
l1=[2,4,6,11,13,14]
nl1={i**2 for i in l if i%2==0} #even
nl2={i**2 for i in l if i%2!=0} #odd
print(nl1)
print(nl2)


'''syntax3:
{true_expression if condition else false_expression for variable in sequence}'''
ll=[2,4,6,11,13,14]
nll={i**2 if i%2==0 else i**3 for i in ll}
print(nll)

'''3-> DICT COMPREHENSION
syntax1:
{key_expression : value_expression for item in collection}
'''
l2=[2,3,4,5,6,7]
dl={i : i**3 for i in l2}
print(dl)

'''syntax2:
{key_expression : value_expression for item in collection if condition}
'''

l=[2,3,4,5,6,7,8]
dll={i:i**3 for i in l if i%2==0}
print(dll)

ll=[45,34,79,91,23]
ddll={i:"pass" for i in ll if i>35}
print(ddll)

'''syntax3:
{key_expression :(true_value_expression if condition else false_value_condition )for item in collection}
'''
ll=[45,34,79,91,23]
ddll={i:("pass" if i>35 else "Fail" )for i in ll }
print(ddll)

d={"amy":90,"ben":45,"chad":36,"ben":29}
dd={i:("pass" if d[i]>45 else "fail")for i in d}
di={k:("pass" if v>45 else "fail")for k,v in d.items()} #getting key value using .items()
print(di)
print(dd)


 








 
