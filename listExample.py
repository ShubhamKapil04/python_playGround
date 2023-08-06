# Duplicate values are allowed in List
mylist = ["apple", "mango", "banana", "cherry", "dragonfruit", "apple1", "apple1"]

for x in mylist:
    print(x)

print(len(mylist))

# Data Type
# It can be String, Integer, Boolean orr all in One List
numberList = [1, 2, 3, 4, 5, 6]

for y in numberList:
    print(y)
print(len(numberList))

allList = [1, 32, "hello", False, True, "World"]

for z in allList:
    print(z)

print(len(allList))

if "hell" in allList:
    print("Yes, hello is in the list of All List")
else:
    print("This word is not in the List")

# print(mylist)