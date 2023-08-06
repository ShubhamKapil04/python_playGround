
import random

import datetime
import timeit


print('-'.join(str(n) for n in range(100)))
print(timeit.timeit("'-'.join(str(n) for n in range(100))", number =100))


# x = random.randint(1, 10)
# print(x)
#
# date = datetime.datetime.now()
# print(date)
#
# DOB = datetime.date(2001, 1, 4)
#
# Today = datetime.date.today()
# age = Today - DOB
# print(age)
