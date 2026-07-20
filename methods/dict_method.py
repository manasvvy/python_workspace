 # access val from dict
d = {1:100, 2:200, 3:300}
print(d[2])

# modify the val from dict
d[2] = 400
print(d)

# methods of dict

# 1) ref.setdefault(key, optional value)
# adds key with given value if key does not exist
# if value is not given, None is stored
d1 = {}
d1.setdefault(1, 100)
d1.setdefault(2)
print(d1)

# 2) ref.get(key)
# returns value of given key
d2 = {11:100, 22:200, 33:300}
print(d2.get(22))

# 3) ref.pop(key)
# removes specified key and returns its value
d2.pop(11)
print(d2)

# 4) ref.popitem()
# removes and returns last inserted key-value pair
item = d2.popitem()
print(item)
print(d2)

# 5) ref.keys(), ref.values(), ref.items()
# keys() -> returns all keys
# values() -> returns all values
# items() -> returns all key-value pairs

d3 = {1:11, 2:22, 3:33}
print(d3.keys())
print(d3.values())
print(d3.items())

# 6) ref.update()
# adds another dictionary into current dictionary
d4 = {9:99}
d3.update(d4)
print(d3)

# 7) ref.clear()
# removes all elements from dictionary
d3.clear()
print(d3)

# 8) len(ref)
# returns number of key-value pairs
print(len(d3))

print("---------")

print(len(d2))
