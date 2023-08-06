
def func(): # we are creating function
    print("We are in the first function")
    def fun1():
        print("This is first child function")
    def fun2():
        print("This is second child function")
    fun2()
    fun1()

func()