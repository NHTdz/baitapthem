def snt(a):
    i = 0
    for y in range(1, a + 1):
        if a % y == 0:
            i += 1
        else:
            continue
    if i == 2:
        return True
    elif a ==1:
        return True
    else:
        return False

lst_day = [1, 7, 11, 21, 40, 2, 15, 20]


for a in lst_day.copy():
    x = snt(a)
    if x == False:
        lst_day.remove(a)
    elif x == True:
        continue
print(lst_day)
