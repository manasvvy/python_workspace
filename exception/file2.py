print("start")
s="muskan"
try:
    n1= int(input("enter no 1"))
    n2= int(input("enter no 2")) 
    print(n1/n2)
    print(s[n2])
except (ZeroDivisionError IndexError ValueError) as e:
    print(e)
 
