
# Else in List Comprehension

list_ = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]

list_s = []

for letter in list_:
    if 'G' not in letter:
        list_s.append(letter)
    else:
        list_s.append('Letter was Skipped')

print(list_s)

print('x' *20)
# Comprehension

list_s1 = [letter if 'G' not in letter else 'Letter was skipped' for letter in list_]
print(list_s1)

print('x' *20)

list_s2 = [letter for letter in list_ if 'G' not in letter]
print(list_s2)
