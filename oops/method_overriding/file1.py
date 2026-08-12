#method overriding using single level instance

from typing_extensions import override
class athlete:         #superclass
    def pushups(self): #instance method
        print("10 warmup pushups")

class wrestler(athlete): #step1
    @override
    def pushups(self):   #step2
        super().pushups()
        print("50 diamond pushups") #step3

w=wrestler()
w.pushups()        
print(wrestler.__mro__)