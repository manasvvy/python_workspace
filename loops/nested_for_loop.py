#print the main dish name with side dish

mains=["idli","dosa","chapati"]
sides=["curry","chutney","sambar"]

for m in mains:
    for s in sides:   #nested
        print(m,"-->",end=" ")
        print(s)
