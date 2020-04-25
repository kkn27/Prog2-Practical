score=float(input("Enter the score: "))
if score < 0:
    print("Invalid")
else:
    if score >100:
        print("Invalid")
    if score >= 50:
        print("Passable")
    if score > 90:
        print("Excellent")
if score < 50:
    print("Bad")