p = 50  # Global variable
def show():
    # This is a NEW local variable.
    # It does NOT affect the global variable.

    p = 100
    print("Inside function (local p):", p)
show()
print("Outside function (global p):", p)
print("-" * 50)
