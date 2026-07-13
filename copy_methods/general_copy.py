l1=[10,20,30,[40,50]]
l2=l1 #general copy

l1[1]=100 #change made using l1
print(l2) #will be reflected on l2

l2[0]=200 #change made using l2
print(l1) #will be reflected on l1

l1[-1].append(80) #changing inner list using l1
print(l1)
print(l2) #will be reflected on l2
