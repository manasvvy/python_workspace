#loop the dict when iterating check if the goal scored is greater than 6,print their names and goals

d={"messi":9,"yamal":1,"mbappe":7,"holland":6}
#get method

for i in d:
    if d.get(i)>6:
        print(i,"=",d.get(i))

for i in d:
    if d[i]>6:
        print(i,"=",d[i])

#nested_collection
'''list of list ("nested list")'''

nl=[["goku",70,45000],["joku",170,40000],["loku",560,105]]
for l in nl:
    if l[1]>100:
        print(l[1]) 
