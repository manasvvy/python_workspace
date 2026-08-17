#relational
class money:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __le__(self, other):
        return self.value <= other.value

    def __ge__(self, other):
        return self.value >= other.value


m1 = money(100)
m2 = money(200)
m3 = money(100)

print(m1 == m2)
print("-----------------------------------------------")

print(m1 != m2)
print("-----------------------------------------------")

print(m1 < m2)
print("-----------------------------------------------")

print(m3 > m2)
print("-----------------------------------------------")

print(m1 <= m3)
print("-----------------------------------------------")

print(m2 >= m1)
