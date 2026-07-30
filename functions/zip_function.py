'''
zip()
IT IS A PREDEFINED FUNCTION THAT COMBINES MULTIPLE ITERABLES ELEMENT BY ELEMENT
SYNTAX=> zip(iterable1,iterable2........)
  ->it accepts two oe more iterables
  ->creates tuple of the corroesponding elements from each iterables
  ->returns a zip object(iterator)
  ->each element produced is a tuple
  ->it is used for pairing or mapping
  ->it stopps at the smallest iterable
'''

names=["amy","ben","chad","den",]
marks=[90,45,36,29]
rollno=[1,2,3,4]
zo=zip(names,marks,rollno)
print(list(zip(names,marks,rollno)))

#di={k:("pass" if v>45 else "fail")for k,v in zip(names,marks,rollno)}
#print(di)

