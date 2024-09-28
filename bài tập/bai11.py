import math

# Lớp TamGiang
class TamGiang:
    def __init__(self, a, b, c):
        self.a = a  # Cạnh thứ nhất
        self.b = b  # Cạnh thứ hai
        self.c = c  # Cạnh thứ ba

    def tinh_dien_tich(self):
        # Sử dụng công thức Heron để tính diện tích
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

# Lớp TamGiangVuong kế thừa từ lớp TamGiang
class TamGiangVuong(TamGiang):
    def __init__(self, a, b):
        # Tam giác vuông có hai cạnh vuông góc
        super().__init__(a, b, math.sqrt(a**2 + b**2))  # Cạnh huyền được tính theo định lý Pythagore
        self.h = b  # Chiều cao (cạnh b)
        self.d = a  # Đáy (cạnh a)

    def tinh_dien_tich(self):
        # Diện tích tam giác vuông = (1/2) * đáy * chiều cao
        return (self.d * self.h) / 2

# Lớp TamGiangCan kế thừa từ lớp TamGiang
class TamGiangCan(TamGiang):
    def __init__(self, a, b):
        # Tam giác cân có hai cạnh bằng nhau
        super().__init__(a, b, a)  # Cạnh thứ ba cũng bằng cạnh a
        self.h = math.sqrt(b**2 - (a / 2)**2)  # Tính chiều cao

    def tinh_dien_tich(self):
        # Diện tích tam giác cân = (1/2) * đáy * chiều cao
        return (self.a * self.h) / 2

# Lớp TamGiangDeu kế thừa từ lớp TamGiangCan
class TamGiangDeu(TamGiangCan):
    def __init__(self, a):
        super().__init__(a, a)  # Tam giác đều có tất cả các cạnh bằng nhau

# Nhập dữ liệu và tính toán

# Nhập thông tin cho tam giác vuông
a_vuong = float(input("Nhập cạnh đáy của tam giác vuông: "))
b_vuong = float(input("Nhập cạnh cao của tam giác vuông: "))

tam_giang_vuong = TamGiangVuong(a_vuong, b_vuong)
print(f"Diện tích tam giác vuông: {tam_giang_vuong.tinh_dien_tich()}")

# Nhập thông tin cho tam giác cân
a_can = float(input("\nNhập cạnh đáy của tam giác cân: "))
b_can = float(input("Nhập chiều cao của tam giác cân: "))

tam_giang_can = TamGiangCan(a_can, b_can)
print(f"Diện tích tam giác cân: {tam_giang_can.tinh_dien_tich()}")

# Nhập thông tin cho tam giác đều
a_deu = float(input("\nNhập cạnh của tam giác đều: "))

tam_giang_deu = TamGiangDeu(a_deu)
print(f"Diện tích tam giác đều: {tam_giang_deu.tinh_dien_tich()}")
