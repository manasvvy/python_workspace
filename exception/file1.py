print(1)
print(2)
print(3)
try:
    print(23/0) #runtime error / exception
except ZeroDivisionError:
    print("handled") 
print(4)  #below lines wont be executed bc its abnormal flow
print(5)
