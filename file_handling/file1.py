f=open("file_handling/demo1.txt","r") #file object is created
print(f.name)
print(f.closed)
print(f.mode)
print(f.readable()) 
print(f.writable())
#print(f.read(5))
print(f.readline(8))
