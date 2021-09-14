# Tính tổng tiền điện theo mức giá
def electric(a):
    used = 0
    cost_level = [1678, 1724, 2014, 2536, 2834, 2927]
    level = [50, 50, 100, 100, 100]
    for i in range(5):
        if a > level[i]:
            used += cost_level[i]* level[i]
            a = a - level[i]
        else:
            used += a*cost_level[i]
            break
    else:
        used += a*cost_level[i+1]
    return used
def thue(electric):
    so_thue = electric * 0.1
    return so_thue

print("Hóa đơn tiền điện")
a = float(input("Nhập vào điện năng tiêu thụ:"))
b = electric(a)
c = thue(electric(a))
total = b +c
print("Số tiền điện:          ", + b,  "đồng")
print("Số tiền thuế gtgt(10%):", + c,   " đồng")
print("Tổng thanh toán:       ", + total,  "đồng" )










