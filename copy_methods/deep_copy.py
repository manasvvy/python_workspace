
import copy
l1=[10,20,30,[40,50]]
l2=l1
l1=copy.deepcopy(l1) #deep copy list done
print(l1)

l1[0]=100 #change using l1
print(l2) #reflected in l2

l1[-1].append(80) #change made using l1
print(l1) #reflected
print(l2) #wont be reflected in l2 bc nested obj are created seprately

