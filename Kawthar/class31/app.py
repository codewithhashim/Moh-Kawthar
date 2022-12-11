# return keyword

# example_function is an identifier
# def is a keyword to define function
# return is a keyword that will give us the value we are getting back after the function runs
def example_function():
    return 34

# print is a function that is calling another function and that function is example_function
print( example_function() )


# The pass statement 
def empty():
    pass

empty()

# (0°C × 9/5) + 32 = 32°F
def temp():
    # code here
    # int is a function
    temp_in_c = int(input("Enter the tempratue in C: "))
    temp_in_f = temp_in_c * 1.8 + 32
    # str is a function 
    print("The temprature in F is: " + str(temp_in_f))

temp()


