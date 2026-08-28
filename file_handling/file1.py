f=open("file_handling/demo1.txt","r") #file object is created
print(f.name)
print(f.closed)
print(f.mode)
print(f.readable())
print(f.writable())
#print(f.read(5))
#print(f.readline(8))
print(f.readlines(8))


print(f.readline(3))
print(f.readline(5))
f.seek(0) #moves the cursor to the expected position 
print(f.tell()) #attribute of the file
f.close()
print(f.closed)