# for loop
# Used to iterate over each element of a sequence or iterable.

l=[10,20,30,40]
for element in l:
    print("gm")

print("-----------------------------------------")

s=(10,20,30,40,50,60,70,80,90,100)
for element in s:
    print("yo")

print("-----------------------------------------")

d={1:10,2:20,3:30,4:40}
for element in d:
    print("hi")

print("-----------------------------------------")

d={1:10,2:20,3:30,4:40}
s=" "
for element in s:
    print("wassup")

print("-----------------------------------------")

l=[10,20,30,40]
t=(22,23,33,34)
st={7,8,9}
d={1:10,2:20,3:30}
s="joe"

# dict.values()
# Returns all values of the dictionary.

for element in d.values():
    print(element)

# dict.items()
# Returns all key-value pairs of the dictionary.

d={1:11,2:22,3:33}
for element in d.items():
    print(element)

# end parameter
# Prints the output on the same line.

for element in s:
    print(element,end=" ")

print()

# range(start, stop, step)
# Generates a sequence of numbers.

for num in range(1,6,1):
    print(num)

for num in range(8,34,2):
    print(num)

for num in range(-8,-34,-2):
    print(num)

print("-----------------------------------------")

# Print only fruits in even index.

fruits=("Mango","kiwi","litchi","grapes","apple","strawberry","blueberry")

'''for num in range(0,7,2):
    print(fruits[num])'''

# startswith()
# Checks whether the string starts with the given substring.

for fruit in fruits:
    if fruit.startswith('g'):
        print(fruit,"starts w G or g")
    else:
        print(fruit,"does not start w G or g")