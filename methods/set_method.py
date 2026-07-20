# Set Methods

# 1) ref.add(object)
# Adds an element to the set

s1=set() 
s1.add(24)
print(s1)

s1=set()
s1.add(75)
print(s1)

# 2) ref.update(collection)
# Adds elements from another collection

s2=set()
s2={22,44}
s1.update(s2)
print(s1)

# 3) ref.pop()
# Removes and returns a random element

s3={2,4,5}
ele=s3.pop()
print(ele)
print(s3)

# 4) ref.remove(object)
# Removes specified element

s4={11,22,33,44}
s4.remove(33)
print(s4)

# 5) ref.discard(object)
# Removes specified element if present

s5={44,55,66,33}
s5.discard(66)
print(s5)

# 6) ref.clear()
# Removes all elements from set

s6=set()
s6.clear()
print(s6)

# 7) ref.issubset()
# Returns True if all elements are present in another set

s7={2,3,4,5}
s8={7,8,9,4,2}
b_v=s7.issubset(s8)
print(b_v)

# 8) ref.issuperset()
# Returns True if set contains all elements of another set

b_v1=s7.issuperset(s8)
print(b_v1)

b_v2=s8.issuperset(s7)
print(b_v2)

# 9) ref.isdisjoint()
# Returns True if sets have no common elements

print(s7.isdisjoint(s8))

# 10) s1.union(s2)
# Returns a new set containing all elements

s9={99,88,77,66}
s10={66,55,44}
us=s9.union(s10)
print(us)

# 11) s1.intersection(s2)
# Returns common elements

cs=s9.intersection(s10)
print(cs)

# 12) s1.difference(s2)
# Returns elements present in first set but not second

ds=s9.difference(s10)
print(ds)

# 13) s1.symmetric_difference(s2)
# Returns uncommon elements

sd=s9.symmetric_difference(s10)
print(sd)
