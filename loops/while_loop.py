#print using while loop numbers from 1 to 7

num=1 #initialization
while num<=7: #condition
    print(num,end=" ")
    num=num+1 #updation (increment/decrement)

print("----------------------------")

#print numbers from 25 to 10
    
numb=25
while numb>10:
    print(numb)
    numb=numb-1 #decrementation
print("----------------------------")

#print using while loop only the even number between 5 to 21

num1=5
while num1<22:
    if num1%2==0:
        print(num1)
    num1=num1+1

print("----------------------------")

#print using while loop only the odd number between 5 to 21

num2=5
while num2<22:
    if num2%2!=0:
        print(num2)
    num2=num2+1

print("----------------------------")

#print only the even numbers in the list
#use index no of list to get the ele
#check if its even
#updation

l=[11,12,15,24,37,40]
i=0 #initialization
while i<6: #while condition
    if l[i]%2==0: #even element condition
        print(l[i])
    i=i+1 #updation

print("----------------------------")
