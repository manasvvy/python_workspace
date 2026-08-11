class employee:
    def work(self):
        print("employee works")

class dev(employee):
    def develop(self):
        print("developer develops")   

class tester(employee):
    def test_code(self):
        print("tests the code")   

class devopsdev(employee):
    def deploy(self):
        print("deploys the code")                  

e=employee()
e.work()
print(employee.__dict__)

d=dev()
d.develop()
print(dev.__dict__)

f=tester()
f.test_code()
print(tester.__dict__) 

dd=devopsdev()
dd.deploy()
print(devopsdev.__dict__)
