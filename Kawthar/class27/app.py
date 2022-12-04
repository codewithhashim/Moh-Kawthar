for x in range(6):
    print(x)
else:
    print("I am gonna be executed after for loop")



# pass
arr = []
for items in arr:
    if arr == []:
        pass
    print(items)

# intentional error
for number in range(25, 26, -4):
    pass

# infinite iterations

# intentional error 2
# arrr=[13,17,22]
for x in []:
 pass


# syntax
# while condition:
    # body of while loop

numa = 10
numb = 20

# comparison operator
while numa <= numb: # wheather numa > numb?
    print(numa)   #print numa
    numa = numa + 1 #add 1 to existing value of numa


month1=28
month2=30

while  month1 <= month2:
    print(month1)
    month1=month1+1






