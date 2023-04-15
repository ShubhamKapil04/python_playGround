lucky_number = [4, 5, 6, 10, 6, 23]
friends = ["kartik", "shubham", "harsh", "karan", "sahil"]
# Extend the list
friends.extend(lucky_number)
# Append th list and put the element in the end
friends.append("Sharma")
# Can add the element in certain index
friends.insert(1, "jaywalk")
# To clear all the data from the list
friends.clear()
# Pop the last element
friends = ["kartik", "shubham", "harsh", "karan", "sahil", "shubham", "Mike", "mike"]
friends.pop()
# Index of the certain object
print(friends.index("Mike"))
# Count of things
print(friends.count("shubham"))
# Sort the List
lucky_number.sort()
print(lucky_number)
# Reverse
lucky_number.reverse()
print(lucky_number)
# Copy
friends2 = friends.copy()
print(friends2)

print(friends)
