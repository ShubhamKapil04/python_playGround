def slicer(myString):
    if myString % 2 == 0:
        return 'EVEN'
    else:
        return myString[0]


name_list = ['Andy', 'Eve', 'Sally']

list(map(slicer, name_list))
