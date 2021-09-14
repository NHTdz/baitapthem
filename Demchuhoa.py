# Nhập vào chuỗi đếm số lượng chữ hoa chữ thường
count_hoa = 0
count_thuong = 0
lst = input("Nhập chuỗi của bạn:")
for x in lst:
    if x.isupper():
        count_hoa +=1
    elif x.islower():
        count_thuong +=1
    else:
        pass
print("Chữ hoa:", count_hoa)
print("Chữ thường:", count_thuong)