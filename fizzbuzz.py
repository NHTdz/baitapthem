a=int(input("Nhập start:"))
b=int(input("Nhập end:"))
for x in range(a,b+1):
    if x%3==0 and x%5==0:
        print(x,"FizzBuzz")
    elif x% 5 == 0:
        print(x,"Buzz")
    elif x% 3 == 0:
        print(x,"Fizz")
    else:
        continue