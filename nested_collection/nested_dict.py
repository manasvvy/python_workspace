#impppppppp


company = {"emp1":{"empid":3,"ename":"zaraki","salary":80000,"dept":"accounts"}, 
        "emp2":{"empid":38,"ename":"piccollo","salary":10000,"dept":"research"},
        "emp3":{"empid":22,"ename":"zach","salary":59000,"dept":"tech"}}

for key,value in company.items():
  # print(value) #ref_var[keys]
    # print(key)   #ref_var.get()
    for key in company:
        inner_dict=company.get(key)  #print (company[key]["ename"])
        print(inner_dict.get("ename")) #company.get(key).get("ename"))

        #for value in company.values():
            #print(value["ename"])
        
for value in company.values():
    if value["salary"]>=30000:
        print(value["salary"])
        print(value["ename"])

    if value["dept"]=="sales" or value["dept"]=="accounts":
        value["salary"]+=5000
print(company)



        
