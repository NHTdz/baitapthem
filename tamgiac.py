# vẽ tam giác vuông dấu *
# Tam giác 1
a=int(input("Nhập kích thuớc tam giác:"))
for i in range(a):
    for j in range(i+1):
        print("*", end="  ")
    print()
# Tam giác 2
b=int(input("Nhập kích thuớc tam giác:"))
for i in range(b,0,-1):
    for j in range(i):
        print("*", end="  ")
    print()
# Tam giác 3
c=int(input("Nhập kích thuớc tam giác:"))
k= 2*c
for i in range(c):
    for j in range(k):
        print(" ",end=(""))
    for h in range(i+1):
        print("*", end=" ")
    k = k - 2
    print()
# Tam giác 4
d=int(input("Nhập kích thuớc tam giác:"))
k=0
for i in range(d,0,-1):
    for j in range(k):
        print(end=" ")
    for j in range(i):
        print("*", end =" ")
    k = k+2
    print()





