# A global variable is declared outside all functions.
# It can be accessed anywhere in the program.

a = 100
def fun():
    # 'global' allows us to MODIFY the global variable.
    # Without it, Python treats 'a' as a local variable.
    global a
    print("Global variable inside the function:", a) # Modifying the global variable
    a += 75
    print("Modified global variable inside the function:", a)
    print("Spain won the FIFA World Cup 2026")


# Function call
fun()
print("Global variable outside the function:", a) # Global variable can also be modified outside the function.
a += 50
print("Modified global variable outside the function:", a)
print("-" * 50)


# ==========================================================
# LOCAL VARIABLE
# ==========================================================

def display():
    # Local variable
    # Exists only inside this function.
    c = 30

    print("Local variable inside the function:", c)

    c += 40

    print("Modified local variable inside the function:", c)


display()

# The following lines will give NameError because
# 'c' exists only inside display().

# print(c)
# c += 50


print("-" * 50)


# ==========================================================
# FUNCTION PARAMETER
# ==========================================================

def display(c):
    # 'c' here is a parameter.
    # It is also a local variable.
    print("Parameter value:", c)

    c += 40

    print("Modified parameter value:", c)


display(30)

print("-" * 50)


# ==========================================================
# EXAMPLE: GLOBAL COUNTER
# ==========================================================

# Global counter
count = 0


def increment_count():
    global count

    count += 1


increment_count()

print("After increment:", count)


def decrement_count():
    global count

    count -= 1


decrement_count()

print("After decrement:", count)

print("-" * 50)

#MODIFYING A GLOBAL VARIABLE

def show():  # Now 'p' refers to the global variable.
    global p
    p -= 20      # 50 -> 30
    p = 100      # 30 -> 100
    print("Inside function (global p):", p)
show()
print("Outside function (global p):", p)

# NOTE:
'''If you try to modify a global variable without using
the 'global' keyword, Python throws:
UnboundLocalError
Example:
p = 50

def show():
     p -= 20

Python assumes 'p' is local because you're assigning to it, but it hasn't been initialized locally.'''
