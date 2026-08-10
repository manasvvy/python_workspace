class book:  #parentclass
    def display_index(self):
        print("every book has index page")

class mathbook(book):  #childclass
    def view_formula(self):
        print("every math book has formulae") 

m=mathbook() #instance of child class
m.view_formula()
m.display_index()
#we can acess parent from child

print(mathbook.__dict__)
print(book.__dict__)
