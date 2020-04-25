ask_item= int(input("Number of items:"))
while ask_item <=0:
    print("Invalid Number")
    ask_item=int(input("Number of items: "))
total_price=0
for i in range(ask_item):
    price_ask=float(input("Price of Items: $ "))
    while price_ask <=0:
        print("Invalid Price")
        price_ask=float(input("Price of items: $"))
    total_price+= price_ask
if total_price > 100:
    print("Total price for 3 items is ${:.2f}".format(total_price * 0.9))
    print("Total price for the products is ${: .2f}".format(total_price))