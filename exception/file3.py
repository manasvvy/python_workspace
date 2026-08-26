#we can have nested try except block in all the outer try exceptelse and finally

print("start")
try:
    try:
        print("innertry")
    except:
        print("innerexcept")
except Exception as e :
    #print(7/0)
    print(e)
else:
    print("yp")
finally:
    print("idgaf")
print("end")    
