import random
import numpy as np
def matrix(m,n):
    lst = [[random.randint(1,10) for e in range(n)]for e in range(m)]
    return lst
def get_flat_list(lst,m,n):
    new_lst =[]
    for i in range(m):
        if i %2 != 0:
            reversed(lst[i])
        new_lst += lst[i]
    return new_lst
m = int(input("Nhập số hàng: "))
n = int(input("Nhập số cột: "))
lst = matrix(m,n)
print(lst)
new_list = get_flat_list(lst,m,n)
print(new_list)
