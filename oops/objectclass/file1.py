class pen:
    pass 

p=pen.__new__(pen)  #step1 __new__ creates empty pen object and returns it
pen.__new__(pen)      #step2 __init__  will initialise the empty pen instance
print(pen)
