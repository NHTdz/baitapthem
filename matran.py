import random
import numpy as np
def matrix(m,n):
    matrix = [[random.randint(1,10) for e in range(n)]for e in range(m)]
    return matrix
m = int(input("Nhập số hàng: "))
n = int(input("Nhập số cột: "))
a =  matrix(m,n)
print(a)
