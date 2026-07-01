# List Methods

# 1) ref.append(object)
# Adds element at the end of the list

l=[20,40,60,80]
l.append(100)
print(l)

# 2) ref.insert(index, object)
# Adds element at specified index

l.insert(0,10)
print(l)

# 3) ref.extend(collection)
# Copies and adds another collection

l2=[200,400]
l3=[11,22]
l2.extend(l3)
print(l2)

l4=[1,2]
l5=[10,20]
nl=l4+l5
print(nl)

# 4) ref.pop()
# Removes and returns last element from collection

l6=[11,22,33,44]
ele=l6.pop()
print(ele)
print(l6)

ele=l6.pop(2)
print(ele)
print(l6)

# 5) ref.remove(object)
# Removes first occurrence of specified element

l7=[10,20,10,30,10,40]
l7.remove(10)

# 6) ref.clear()
# Removes all elements from list

l8=[90,70]
l8.clear()
print(l8)

# 7) ref.count(object)
# Returns number of occurrences of object

l9=[11,22,11,11,11]
number=l9.count(11)
print(number)

# 8) ref.index(object)
# Returns index of first occurrence of object

l10=[11,22,11,11,11]
index=l10.index(11)
print(index)

# 9) ref.sort()
# Sorts list in ascending order

l12=[100,11,55,99]
l12.sort()
print(l12)

# 10) ref.reverse()
# Reverses the list

l12.reverse()
print(l12)