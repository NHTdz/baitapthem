count = ai = ai_1 = 0
n = int(input("Nhập vị trí số cần tìm:"))
while count<n:
    ai_1 += 1
    string_ai = str(ai)
    string_ai_1 = str(ai_1)
    for i in(string_ai):
        for j in(string_ai_1):
            if i == j:
                break
        if i == j:
            break
    else:
        ai = ai_1
        count +=1
print(ai)

