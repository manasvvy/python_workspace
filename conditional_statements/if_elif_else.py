print("start")
age=int(input("enter ur age"))
if age>1 and age<13:
    print("child")
elif age>=13 and age<18:
    print("teen")
elif age>=18 and age<31:
    print("adult")
elif age>=31 and age<60:
    print("super adult")
elif age>=61 and age<=120:
    print("senior citizen")
else:
    print("invalid age")
print("end")
