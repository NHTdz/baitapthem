string_ = str(input("Nhập chuỗi:"))
string_reversed = string_[::-1]
if string_reversed == string_:
    print(string_ + " là chuỗi đối xứng")
else:
    print(string_ + " không là chuỗi đối xứng")