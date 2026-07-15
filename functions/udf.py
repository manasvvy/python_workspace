'''#function without parameter and without return

def show(): #function declaration
    print("function without parameter and returm") #function
show() #function call    
print(show)

def announce_mock():
    print("mock will be cunducted on saturday")
    print("please perform well")
announce_mock()    


#without parameter and with return

def get_weather_info():
    print("u r welcome to todays report")
    return "temp is 23"
temp=get_weather_info() #storing functionname and then printing
print(temp)
print(get_weather_info()) 

def return_money():
    return 99
m= return_money()
print(m)

#with parameter and without return

def book_my_show(theater,movie,price):
    print(f"{moviename}movie is displayed in {theatername}theater for {ticketprice}")
book_my_show("nexus mall theater", "superman", 500)    #actual values
book_my_show("dcl", "batman", 1500)    #actual values'''


#with parameter and with return

def send_otp(phoneno):
    print("send otp to this phoneno")
    return 1234
otp=send_otp(4522154585)
print(otp)

#print(send_otp(4522154585))

def wish(name):
    print(f"hbd {name}")
    return "truffle cake"
print(wish("j"))

def operations(a,b):
    return a+b, a-b, a*b, a/b
print(operations(4,2))

def add(a,b):
    return a+b 
print(add(4,2))

def sub(a,b):
    return a-b
print(sub(4,2))

def multiply(a,b):
    return a*b
print(multiply(4,2))

def div(a,b):
    return a/b
print(div(4,2))













