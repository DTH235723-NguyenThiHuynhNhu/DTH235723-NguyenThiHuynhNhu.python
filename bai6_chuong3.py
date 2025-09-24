n = int(input("Nhập số n (tối đa 2 chữ số): "))

don_vi = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
chuc = ["", "mười", "hai mươi", "ba mươi", "bốn mươi",
        "năm mươi", "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]

if n < 10:
    print(don_vi[n])
else:
    hang_chuc = n // 10
    hang_dv = n % 10
    if hang_dv == 0:
        print(chuc[hang_chuc])
    else:
        print(chuc[hang_chuc], don_vi[hang_dv])