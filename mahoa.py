# mã hóa
# bạn cần nhập vào nội dung và khóa k
cn = str(input("Chọn chức năng(mahoa or giaima):"))
k = int(input("Nhập vào khóa k:"))
if cn == "mahoa" or cn == "giaima":
    text= str(input("Nhập văn bản bạn cần xử lí:"))
    arr=text.split(" ")
    for i in range(0,len(arr)):
        #tách theo khóa k + mã hóa
        mahoa = arr[i][k-1::-1]+arr[i][:k-1:-1]
        print(mahoa, end=" ")
else:
    print("No")