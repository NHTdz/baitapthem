while True:
    a = int(input("Nhập số:"))
    i = 0
    for y in range(1,a+1):
        if a%y == 0:
            i+=1
        else:
            continue
    if i == 2:
        print(a,"là số nguyên tố")
    else:
        print(a, "không là số nguyên tố")
    hoi = input("bạn muốn kiểm tra tiếp không(y/n):")
    if hoi == "n":
        print("cám ơn")
        break