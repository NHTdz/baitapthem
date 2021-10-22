'''[Bài tập] Quản lý thông tin học viên

Xây dựng ứng dụng quản lý thông tin học viên. Một học viên bao gồm những thông tin: Mã số, họ tên, giới tính, tỉnh/Thành phố, điểm thi lý thuyết, điểm thi thực hành (điểm thi cao nhất là 100, thấp nhất là 0).

Người dùng có thể thực hiện các chức năng sau:

1. Thêm thông tin học viên vào bộ nhớ

2. Cập nhật thông tin học viên

3. Hiển thị danh sách tất cả học viên

4. Hiển thị danh sách học viên thi đỗ (Điểm trung bình >= 75)

5. Hiển thị danh sách học viên thi trượt (Điểm trung bình < 75)

6. Xóa thông tin của học viên'''
# DS có sẵn
inf_list = '''001,Nguyễn Thăng,Nam,Hải Dương,90,95
002,Nguyễn Thăng,Nam,Hải Dương,70,80
003,Nguyễn Thăng,Nam,Hải Dương,80,60'''
# Các sự lựa chọn
def display():
    print('''Các danh mục của chương trình:
    1. Thêm thông tin học viên vào bộ nhớ

    2. Cập nhật thông tin học viên
    
    3. Hiển thị danh sách tất cả học viên
    
    4. Hiển thị danh sách học viên thi đỗ (Điểm trung bình >= 75)
    
    5. Hiển thị danh sách học viên thi trượt (Điểm trung bình < 75)
    
    6. Xóa thông tin của học viên
    
    7. Thoát chương trình ''')
def choice():
    userchoice=input("Nhập lựa chọn của bạn:")
    return userchoice
# 1. lưu tt
def save_infor():
    pass
# 2. thêm tt
def update_infor(inf_list):
    show_header()
    while True:
        add = input("Nhập thông tin:")
        test = add.split(",")
        if int(test[4]) >100 or int(test[4]) <0 or int(test[5]) >100 or int(test[5]) <0:
            print("Bạn nhập điểm sai rồi, nhập lại thôi")
            continue
        inf_list += "\n" + add
        hoi = input("bạn có muốn nhập thêm(y/n):")
        if hoi == "n":
            break
    return inf_list
# hiển thị header
def show_header():
    print(f"{'Mã số':<5}{'Họ tên':^20}{'Giới tính':^9}{'Tỉnh/Thànhphố':^15}{'Điểm thilý thuyết':^20}{'Điểm thi thực hành':^20}")
# hàm inf condition
def infor(condition):
    show_header()
    lst = inf_list.split("\n")
    for stt in lst:
        if stt == "":
            continue
        inf = stt.split(",")
        id = inf[0]
        name = inf[1]
        sex = inf[2]
        province = inf[3]
        theory = inf[4]
        practice = inf[5]
        is_value= condition(theory,practice)
        if is_value:
            print(f"{id:<5}{name:^20}{sex:^9}{province:^15}{theory:^20}{practice:^20}")
# ĐK cho hàm 3
def get_all(theory,practice):
    return True
# điểm tb
def medium_score(theory,practice):
    avg=(int(theory)+int(practice))/2
    return avg
# ĐK cho hàm 4
def pass_condition(theory,practice):
    return medium_score(theory,practice) >= 75
# ĐK cho hàm 5
def fail_condition(theory,practice):
    return medium_score(theory,practice) < 75
# 3. hiện thị all
def show_infor():
    infor(get_all)
# 4. hiển thị pass
def infor_passed():
    infor(pass_condition)
# 5. hiển thị fail
def infor_failed():
    infor(fail_condition)
# 6. xóa failed
def delete_failed(inf_list):
    delete = input("Nhập mã số bạn cần xóa:")
    lst = inf_list.split("\n")
    new_inf_list = ""
    for std in lst:
        infor = std.split(",")
        id = infor[0]
        if delete != id:
            new_inf_list += std + "\n"
    return new_inf_list


# main program
while True:
    display()
    person_choice = choice()
    print("Bạn chọn:"+ person_choice)
    if person_choice == "1":
        save_infor()
    elif person_choice == "2":
        inf_list= update_infor(inf_list)
    elif person_choice == "3":
        show_infor()
    elif person_choice == "4":
        infor_passed()
    elif person_choice == "5":
        infor_failed()
    elif person_choice == "6":
        inf_list=delete_failed(inf_list)
    elif person_choice == "7":
        break


