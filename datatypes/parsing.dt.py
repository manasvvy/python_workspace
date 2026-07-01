#bool()
#Converts a value into Boolean (True or False)

print(bool(3))
print(bool(0.0))
print(bool([0.0]))
print(bool(" "))
print(bool(0.1j))

print("-------------")

#Explicit Type Casting
#Converts one datatype into another using predefined functions.

s="10"
print(int(s))

s2="10.10"
print(float(s2))

s3="10j"
print(complex(s3))

s4="False" 
print(bool(s4))

#when str having bool is explicitly typecasted we alwas get the value True
#to overcome this we use eval()
