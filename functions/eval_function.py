
#eval()
#Evaluates a string as a Python expression and returns the result

result=eval("5+8")
print(result)
print(type(result))

a=10
b=20
print(eval("a-b"))

l=[10,20,30,40]
print(eval("len(l)+3"))

print(type(eval("()")))

print("-----------")
citizen=eval(input("r u indian"))
print(citizen)
print(type(citizen))


#concatination joining 2 or more strings into a single continous string it is achieved using + operator
f="dragon "
l="fruit"

v=f+l
print(v)

country=input("enter country")
score=int(input("enter runs"))
over=float(input("enter overs"))
print(country+" score"+str(score)+" runs"+str(over)+" overs")

#f-string
#Formats a string by embedding variables directly using {}

sen=f"{country} scored {score} runs in {over} over"
print(sen)

#format()
#Formats a string by replacing {} placeholders with values.


sen2="{} scored {} runs in {} over".format(country,score,over)
print(sen2)
