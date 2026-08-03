'''DUNDER VARIABLES

-> Short form for Double Underscore.
-> Dunder variables are predefined special variables with double underscores at the start and end.
-> These variables are automatically created by Python. 
-> They help in identifying modules.
-> Track where the file is stored.
-> Control how the module behaves when they are imported.
-> For providing documentation.

Dunder Variables:
1. __name__
2. __file__
3. __cached__
4. __package__
5. __doc__


1. __name__

-> It represents the name of the module.
-> If the Python module/file is executed directly, then this variable will be assigned with the value "__main__".

Note:
If the module having the __name__ variable is executed because of importing, then that module name will be assigned as the value to __name__.

Purpose:
To prevent/avoid certain code from getting executed, we use a conditional block.

Syntax:

if __name__ == "__main__":
    # Only testing code should get executed

Example:

print(__name__)

Output:
__main__      -> when the file is executed directly.
module name   -> when the file is executed because of importing.'''
