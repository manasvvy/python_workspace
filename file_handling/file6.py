f=open("file_handling/demo5.txt","a+")
f.write("v is handsome")
f.seek(0)
print(f.read())
