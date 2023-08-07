
# def chess_ans_bun(original_fun):
#
#     def wrap():
#         print('I am upper bread')
#         original_fun()
#         print('I am lower bread')
#     return wrap()
# def chicken():
#     print('I am roasted chicken')
#
#
# burger = chess_ans_bun(chicken())
# # burger()

# chicken()

# we can import another function from the file and use is as decorator

# def divide(x, y):
#     print(x/y)
# from functions import say_hi
# def outer_div(func):
#     def inner(x, y):
#         if(x < y):
#             x,y = y, x
#             return func(x, y)
#     return inner
# @outer_div
# # divide1 = outer_div(divide)
# # divide(2, 4)
# def divide(x, y):
#     print(x/y)


# Returning a Function as a Value

# def greeting(name):
#     def hello():
#         return f"Hello, {name} !"
#     return hello()
#
# greet = greeting("Shubham")
# print(greet)


def make_pretty(func):
    # define the inner function
    def inner():
        # add some additional behavior to decorated function
        print("I got decorated")
        # Call original Function
        func()
    # returning the inner function
    return inner

# define ordinary Function
@make_pretty
def ordinary():
    print("I am Ordinary")

ordinary()

# decorate the ordinary function
# decorated_func = make_pretty(ordinary)
# decorated_func()
