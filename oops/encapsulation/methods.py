#setter and getter methods

class student:
   def __init__(self,marks,fees):
      self.__marks=0 #pvt iv
      self.__fees=0

   def get_marks(self): 
      return self.__marks

   def set_marks(self,marks):
    if marks>=0 and marks<=100: #validation logic
       self.__marks=marks       #initialising logic
    else:
       print("invalid")   

   def get_fees(self):
      return self.__fees

   def set_fees(self,fees):
      if fees>=0 and fees<=50000000:
         self.__fees=fees
      else:
         print("go to other school")   
          

s1=student()
s1.set_marks(88)           
print(s1.get_marks())
s1.set_fees(800000000000008)           
print(s1.get_fees())
 