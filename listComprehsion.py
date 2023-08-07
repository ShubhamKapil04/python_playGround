
# List Comprehension

# num = [1, 2, 3, 4, 5, 6, 7]
# sqr_nums1 = []
# for x in num:
#     sqr_nums1.append(x**2)
# print(sqr_nums1)
#
# print('x' * 20)
#
#
# sqr_nums2 = [x**2 for x in num]
# print(sqr_nums2)

# name = []
# for letter in 'Shubham':
#     name.append(letter)
# print(name)
#
# name1 = [letter for letter in 'Shubham']
# print(name1)

# Condition in List Comprehension

# even = []
# for x in range(10):
#     if x % 2 != 0 :
#         even.append(x)
# print(even)
#
# # List Comp
#
# even = [x**2  for x in range(10) if x%2 == 0]
# print(even)

# Nested Loop

my_list = []
for x in [2, 4, 6]:
    for y in [1, 3, 5]:
        my_list.append(x*y)

print(my_list)

my_list2 = [x*y for x in [2, 4, 6] for y in [1, 3, 5] if x*y != 20 if x*y != 10]
print(my_list2)

