'''#print the main dish name with side dish

mains=["idli","dosa","chapati"] 
sides=["curry","chutney","sambar"]

for m in mains:
    for s in sides:   #nested
        print(m,"-->",end=" ")
        print(s)

#
l=[5,6,7]
for i in l:
    for j in range(1,11,1):
        #print(i,"*",j,"=",i*j)
        print(f"{i}*{j}={i*j}")'''

#print only the names whos salary is greater than 10000

ll=[["jake",10,25000],["ben",24,10000],["chad",15,70000]]
print(ll)
for il in ll:
    if il[2]>10000 and il[2]<40000:
        print(il[0].upper())
