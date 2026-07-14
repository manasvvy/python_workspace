#function without parameter and without return

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
    print(f"{movie}movie is displayed in {theater}theater for {rupees} rupees")
book_my_show("nexus mall theater", "superman", 500)    #actual values
book_my_show("dcl", "batman", 1500)    #actual values


#with parameter and with return

