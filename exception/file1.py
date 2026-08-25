print(1)
print(2) 
print(3)
l=[10,20,30]
try:
    print(l[4]) #runtime error / exception
    print("line1")
except IndexError as e:
    print(8/0)
    print("handled")
print(4)  #below lines wont be executed bc its abnormal flow
print(5)
