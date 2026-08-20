from abc import ABC,abstractclassmethod #step1

class emp(ABC): #step2 emp is subclass of abc
    @abstractclassmethod
    def work(self): #work abstract method
        pass

#e=emp() cant create instance for abstract classes


class actress(ABC): #step2 actress is subclass of abc
    @abstractclassmethod
    def act(self): #work abstract method
        pass
    @abstractclassmethod
    def dance(self):
        pass