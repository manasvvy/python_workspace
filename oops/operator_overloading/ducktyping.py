class sms: 
    def msg(self):
        print("sms")

class whatsapp:
    def msg(self):
        print("whatsapp msg")        

class insta:
    def msg(self):
        print("insta dm")  

class telegram:
    def msg(self):
        print("telegram msg")        

def communication(msg_app):
    if hasattr(msg_app,"msg"):
        msg_app.msg()

m1=sms()
m2=whatsapp()
m3=insta()
m4=telegram()

l=[m1,m2,m3]
l.append(m4)
for apps in l:
    apps.msg() #invoking
    #communication(apps)

print(hasattr(m1,"msg"))    
        
