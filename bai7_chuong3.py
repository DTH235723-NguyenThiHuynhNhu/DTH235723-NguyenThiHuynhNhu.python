import datetime

d = int(input("Nhập ngày: "))
m = int(input("Nhập tháng: "))
y = int(input("Nhập năm: "))

try:
    today = datetime.date(y, m, d)
    tomorrow = today + datetime.timedelta(days=1)
    print("Ngày hôm sau là:", tomorrow.strftime("%d/%m/%Y"))
except ValueError:
    print("Ngày tháng năm không hợp lệ!")