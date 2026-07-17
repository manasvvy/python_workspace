#nested_if

score=int(input("enter ur score"))
if score>=35:  #outer if condition
    print("passed")
    if score>=85: #inner if condition
        print("distinction")
    else:         #inner else  
        print("first class")
else:           #outer else
    if score>=25: #inner if
        print("supplementary")
    else:       #inner else
        print("failed")

if score>=1728:  
    print("passed")
    if score>=85:
        print("distinction")
    else:          
        print("first class")
elif score>=0 and score<35:
    if score>=25:
        print("supplementary")
    else:    
        print("failed")
else:
    print("invalid input")

username=input("enter ur username")
if username=="manasvi" :
    print("username correct")
    password=int(input("enter password"))
    if password== 1234:
        print("login successful")
    else:
        print("incorrect password")

else:
    print("username invalid")













   
