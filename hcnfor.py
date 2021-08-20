kitu = input('Nhập kí tự: ')
w = int(input('Nhập CR: '))
h = int(input('Nhập CD: '))

for i in range(1,h + 1):
    kitur  = ''
    for j in range(1,w + 1):
        if i == 1 or i == h:
            kitur += kitu
        else:
            if j == 1 or j == w:
                kitur +=kitu
            else:
                kitur += ' '
    print(kitur)
kitu = input('Nhập kí tự: ')
w = int(input('Nhập CR: '))
h = int(input('Nhập CD: '))
for i in range(h):
    for j in range(w):
        if i == 0 or i == h-1 or j ==0 or j ==w-1:
            print(kitu,end=" ")
        else:
            print(" ",end=" ")
    print()