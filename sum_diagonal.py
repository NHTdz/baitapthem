import random
import numpy as np
def matrix(m,n):
    lst = [[random.randint(1,10) for e in range(n)]for e in range(m)]
    lst = np.array(lst)
    return lst
def sum_diagonal(lst,m,n):
    sum = 0
    for i in range(m):
        for j in range(n):
            if i == j:
                sum += lst[i][j]
    return sum
m = int(input("Nhập số hàng: "))
n = int(input("Nhập số cột: "))
lst = matrix(m,n)
print(lst)
sum= sum_diagonal(lst,m,n)
print(sum)
