#CÁCH1
a = int(input("số nguyên tố cần hiển thị:"))
b =0
for x in range(1,1000000000):
    c=0
    for y in range(1, x):
        if x % y == 0:
            c += 1
    if c == 1:
        print(x, end=",")
        b +=1
        if b==a:
            break
#CÁCH2
def songuyento(n):
    for i in range(2,n):
        if (n%i ==0):
            return False;
    return True
n = int(input("Nhập số ngto cần hiển thị:"))
dem = 0
i = 2
while dem <n:
    if songuyento(i):
        dem += 1
        print(i, end = ", ")
    i +=1


