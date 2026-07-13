import copy
l1=[10,20,30,[40,50]]
l2=copy.copy(l1)
print(l2)

l1[0]=100 #change using l1
print(l2) #change is not reflected

l1[-1].append(80) #changing nested object using l1
print(l2) #change will be reflectedon l2
