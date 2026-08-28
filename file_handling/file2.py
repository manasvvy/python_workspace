l=["im a barbie girl\n","in the barbie world\n","life in plastic is fantastic"]


f=open("file_handling/demo2.txt","w")
f.write("charging")
print(f.tell())
f.seek(0)
f.write("bye")
'''f.write("today hectic\n")
f.write("we in 2026\n")
f.writelines(l)'''
f.close()
print(f.closed)