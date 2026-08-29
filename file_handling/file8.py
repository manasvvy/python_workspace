class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f"{self.name} {self.age}"    

s=student("chandu",55)        
import pickle
with open("file_handling/demo6.pkl","w+b") as f:
    bin_data=pickle.dumps(s)
    f.write(bin_data)
    f.seek(0)
    data=f.read()
    python_object=pickle.loads(data)
    print(python_object)
