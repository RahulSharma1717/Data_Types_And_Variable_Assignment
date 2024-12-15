# 1) Store an integer value in a variable name age and find its type using type function.

age = 100
print(type(age))

# Output: <class 'int'>


# 2) Store a number in string form so that the data type of the number is string

alpha = "12345"
print(type(alpha))

# Output: <class 'str'>


# 3) Does the data type of a variable change when the value inside the variable changes?

x = 10          # x is an integer
print(type(x))  # Output: <class 'int'>

x = 10.5        # x is now a float
print(type(x))  # Output: <class 'float'>

x = "Hello"     # x is now a string
print(type(x))  # Output: <class 'str'>



