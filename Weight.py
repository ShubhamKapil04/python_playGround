weight = int(input("Weight: " ))

unit = input("(K)g or (L)bs: ")

if unit.upper() == "K":
    coverted = weight / 0.45
    print("Weight is Lbs: " + str(coverted))
else:
    converted = weight * 0.45
    print("Weight in Kg: " + str(converted))