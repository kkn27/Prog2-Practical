sales = int(input("Enter Sales"))
if sales < 1000:
    first_bonus = sales * 0.1
    print ( first_bonus)
elif sales >= 1000:
    second_bonus =sales * 0.5
    print (second_bonus)