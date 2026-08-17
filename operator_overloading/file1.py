#arithmetic
class money:
    def __init__(self,value):
        self.value=value

    def __add__(self,other):
        return money(self.value + other.value) #return a money instance and after that override the moneyvalue instead address

    def __sub__(self,other):
            return money(self.value - other.value)


    def __mul__(self,other):
            return money(self.value * other.value)


    def __truediv__(self,other):
            return money(self.value / other.value)


    def __floordiv__(self,other):
            return money(self.value // other.value)



    def __mod__(self,other):
            return money(self.value % other.value)


    def __pow__(self,other):
            return money(self.value ** other.value)


    def __str__(self):
        return f"{self.value}" #override str returns actual value instead of address



m1=money(100)
m2=money(200)
m3=money(500)

print(m1+m2+m3)
print("-----------------------------------------------")

print(m3-m1)
print("-----------------------------------------------")

print(m2*m1)
print("-----------------------------------------------")

print(m3/m1)
print("-----------------------------------------------")

print(m3//m2)
print("-----------------------------------------------")

print(m2%m1)
print("-----------------------------------------------")

print(m2**m3)
