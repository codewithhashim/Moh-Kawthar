# def is a keyword / identifier ()
name = "Kaw"
# parameter
def functionName (name):
    # built in function () 
    print (name)

# argument
# functionName(name)



# day = 24
def date(day):
    print(day)

# date(4555)


# lambda (keyword) -> anonymous function

# 
# lambda parameter : expression
a = 45
ab = lambda a, b : a+b
# print(ab (a, 45))

aa = 4556
# if you print it like this it will return the address of the function 
# print( lambda aa : aa + 3 )


def names():
   lae = lambda aaa, bbb : aaa - bbb
   return lae(435, 67)

# print(names())
# initt = names()
# print(initt)


# kaw = lambda aaa, bbb : aaa - bbb
print(names() )

# Scope

# isTure=True

def print_true ():
    isTrue = 45

print(print_true())
# Problem is scope
print(isTrue)