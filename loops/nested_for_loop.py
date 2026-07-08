#print the main dish name with side dish

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
        print(f"{i}*{j}={i*j}")
    
