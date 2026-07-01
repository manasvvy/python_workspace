# Type Casting
# Type casting is the process of converting one datatype into another datatype.

# 1) Implicit Type Casting
# Conversion is done automatically by Python.

b=True
i=10
f=1.1
c=5j

print(b+i)
print(b+f)
print(f+c)
print(i+f)
print(i+c)
print(f+c)

print(bool(i))
print(bool(c))
print(bool(f))

# 2) Collectors
# Used to convert one collection into another collection.

l=[10,20,30]
print(tuple(l))
print(set(l))
print(str(l))
# print(dict(l))  # Not possible because dict expects key:value pairs

t=(10,20,30)
print(tuple(t))
print(set(t))
print(str(t))

d={1:10,2:20,3:30}
print(tuple(d))
print(set(d))
print(str(d))