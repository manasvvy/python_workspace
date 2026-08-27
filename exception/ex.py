class InvalidMarksException(Exception):
    pass
class InvalidAgeException(Exception):
    pass

class student:
    def __init__(self,name,):
        self.name=name

    def set(self,marks):
        if marks<=100:
            raise InvalidMarksException("invalid")            
        else:
            print("done")

    def age(self,marks):
        if marks<=100:
            raise InvalidMarksException("invalid")            
        else:
            print("done")
          