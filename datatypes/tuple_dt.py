# Tuple Datatype
# Ordered collection of elements
# Immutable datatype
# Represented using ()

t=(10,20,30,50)
print(type(t))
print(len(t))

# 1) ref.count(object)
# Returns number of occurrences of object

t2=(20,30,40,50)
number=t2.count(20)
print(number)

# 2) ref.index(object)
# Returns index of first occurrence of object

ind=t2.index(20)
print(ind)