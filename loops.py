for i in range(1,21,2):
    print(i,end='')
print ()
for i in range(0,110,10):
    print(i,end="")
print()
num=int(input("Enter a number:"))
list=[]
for i in range (1, num+1):
    list.append("*"*i)
print("\n".join(list))

n=int(input("Number of star:"))
for i in range(0,n):
    print("*",end="")