import sys
# Generators
def my_gen(n:int):
    start = 0
    while start < n:
        print(f'My_range is returning:{start}')
        yield start
        start += 1

gen_list = my_gen(10)
print(next(gen_list))
print(next(gen_list))
print(next(gen_list))
print(next(gen_list))

print('x' * 20)
print(f'This gen_list takes {sys.getsizeof(gen_list)} bytes')

itr_list = []

for val in gen_list:
    itr_list.append(val)
print(f'This normal_list takes {sys.getsizeof(itr_list)} bytes')



# Normal Function
# def fun():
#     return value