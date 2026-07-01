# Slicing
# The process of extracting a part/portion from a sequence type collection is known as slicing.
# Slicing can be done only on index-based (ordered) collections.

# Syntax
# sequence[start : stop : step]

# start -> Starting index
#          Inclusive
#          Default = 0

# stop -> Ending index
#         Exclusive
#         Default = len(sequence)

# step -> Number of positions to move after each element
#         +ve : Left to Right
#         -ve : Right to Left
#         Default = 1

l=[10,20,30,40,50,60]


sl=[20, 30, 40]
sl=l[1:4:+1]
print(sl)

sl1=[20, 40, 60]
sl1=l[1:6:+2]
print(sl1)

sl2=[60]
sl2=l[-1:]
print(sl2)

sl3=[60, 50, 40, 30, 20, 10]
sl3=l[::-1]
print(sl3)

sl4=[50, 40, 30]
sl4=l[4:1:-1]
print(sl4)

sl5=[50, 20]
sl5=l[4::-3]
print(sl5)
