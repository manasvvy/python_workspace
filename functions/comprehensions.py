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
