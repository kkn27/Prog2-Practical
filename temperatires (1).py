Menu= "Menu \n C = Convert Celsius to Fahrenheit \n F= Convert Fahrenneit to Celsius \n Q=Quit"
print(Menu)
choice = input(">>>").upper ()
while choice != "Q":
    if choice == "C":
        ask_celsius = float (input("Celsius: "))
        calculate_fahremheit = ask_celsius * 9/5 + 32
        print("Result: {:.2f} C".format(calculate_fahremheit))
    elif choice == "F":
        ask_fahrenheit = float (input("Fahrenheit: "))
        calculate_celsius = 5/9 * (ask_fahrenheit - 32)
        print("Result: {:.2f} C".format(calculate_celsius))
    else:
        print("Invalid option")
    print(Menu)
    choice=input(">>>").upper()
print("Thank You")