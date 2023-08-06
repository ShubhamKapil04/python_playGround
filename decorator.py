
def chess_ans_bun(original_fun):

    def wrap():
        print('I am upper bread')
        original_fun()
        print('I am lower bread')
    return wrap()
def chicken():
    print('I am roasted chicken')


burger = chess_ans_bun(chicken())
# burger()

# chicken()
