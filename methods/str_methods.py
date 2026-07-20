name="manasvi"
print(name) 
print(type(name))
print(len(name))

#methods
#1)ref.capitalize() returns new str only 1st char will be capitalized

s1="python"
print(s1.capitalize())

#2)ref.title() first letter of each word will be upper case letter

s2="python java javascript"
print(s2.title())

#3)ref.startswith() checks if substring is matching is case sensitive it returns bool value

s3="Mathematics"
print(s3.startswith("Mat"))

#4)ref.endswith() Checks whether the string ends with the given substring and returns a boolean value.

s4="Biology"
print(s4.endswith("logy"))

#5)ref.uppercase Converts all characters to uppercase

s5="Biology"
print(s5.upper())

#6)ref.lower() Converts all characters to lowercase
print(s5.lower())

#7)ref.isupper() Returns True if all characters are uppercase
print(s5.isupper())

#8)ref.islower() Returns True if all characters are lowercase.
print(s5.islower())

#9)string.swapcase() Converts uppercase letters to lowercase and vice versa
s6="PSYchology"
print(s6.swapcase())

#10)string.count()  Returns the number of occurrences of a substring
print(s6.count("o"))

#11)string.index() Returns the index of the first occurrence of a substring.
s7="malayalam"
print(s7.index("l"))

#12)string.isalpha() Returns True if all characters are alphabets.
print(s6.isalpha())

#13)string.isdigit() Returns True if all characters are digits
s8="258963147"
print(s8.isdigit())

#14)string.isalnum() Returns True if all characters are alphabets or digits
s9="fifa26"
print(s9.isalnum())

#15)string.replace() Replaces a substring with another substring
print(s9.replace("fifa","fafi"))

#16)string.lstrip() Removes leading spaces from the left side.
s10="     hi"
print(s10.lstrip())

#17)string.rstrip() Removes trailing spaces from the right side.
s11="hi      "
print(s11.rstrip())

#18)string.strip() Removes leading and trailing spaces.
s12="    rainy szn    "
print(s12.strip())

#19)string.split() splits based on space and returns a list of words
s13="i have super powers"
print(s13.split())

#20)string.join() iterable takes all items in an collection and joins
l=["25", "6", "2026"]
print("/".join(l))

s14="he is a good boy"
print(len(s14.split()))



