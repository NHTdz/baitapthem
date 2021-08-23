a = int(input("Nhập dung lương file(byte):"))
b = a//4096
c = a%4096
if c == 0:
    print("Dung lượng file chiếm trên ổ đĩa là:", b * 4)
else:
    print("Dung lượng file chiếm trên ổ đĩa là:", (b * 4)+4)