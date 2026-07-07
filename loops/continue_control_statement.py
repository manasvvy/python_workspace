#print numbers from 7 to 28 using for loop

for i in range(7,29):
    print(i,end=" ") 


#print numbers from 7 to 28 using for loop but even numbers should be skipped

for i in range(7,29):

    if i%2==0:
        continue
    print(i,end=" ")


#print only the positive marks ignore negative marks

l=[720,210,-7,-21,420,512]
for ele in l:
    if ele<0:
        continue
    print(ele)


#skip the char 'e' in s
    
s="xylemphloemtrachae"
for char in s:
    if char=="e":
        continue
    print(char,end="")

#get a new str the output should be xylmphlomtracha

s="xylemphloemtrachae"
s1="xylmphlomtracha"
for s in s1:
    if s1=="xylmphlomtracha":
        continue
    print(s1,end="")

