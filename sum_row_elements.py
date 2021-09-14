import random
import numpy as np
def matrix(m,n):
    lst = [[random.randint(1,10) for e in range(n)]for e in range(m)]
    lst = np.array(lst)
    return lst
def sum_row_elements(a,m):
    sum = [0,]
    for i in range(m):
        sum += a[i]
    return sum
m = int(input("Nhập số hàng: "))
n = int(input("Nhập số cột: "))
a = matrix(m,n)
tup = tuple(sum_row_elements(a,m))
print(a)
print(tup)

