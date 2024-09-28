import math

# Lớp Điểm
class Diem:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def display(self):
        print(f"Tọa độ điểm: ({self.x}, {self.y})")

# Lớp Elip kế thừa từ lớp Điểm
class Elip(Diem):
    def __init__(self, x, y, ban_truc_lon, ban_truc_nho):
        super().__init__(x, y)
        self.ban_truc_lon = ban_truc_lon  # Bán trục lớn
        self.ban_truc_nho = ban_truc_nho  # Bán trục nhỏ

    def tinh_dien_tich(self):
        return math.pi * self.ban_truc_lon * self.ban_truc_nho

# Lớp Đường Tròn kế thừa từ lớp Elip
class DuongTron(Elip):
    def __init__(self, x, y, ban_kinh):
        # Đường tròn có bán trục lớn và bán trục nhỏ bằng nhau, đều là bán kính
        super().__init__(x, y, ban_kinh, ban_kinh)
        self.ban_kinh = ban_kinh

    def tinh_dien_tich(self):
        return math.pi * (self.ban_kinh ** 2)

# Nhập dữ liệu và tính toán

# Nhập thông tin cho hình elip
x_elip = float(input("Nhập tọa độ x của elip: "))
y_elip = float(input("Nhập tọa độ y của elip: "))
ban_truc_lon = float(input("Nhập bán trục lớn của elip: "))
ban_truc_nho = float(input("Nhập bán trục nhỏ của elip: "))

elip = Elip(x_elip, y_elip, ban_truc_lon, ban_truc_nho)
elip.display()
print(f"Diện tích elip: {elip.tinh_dien_tich()}")

# Nhập thông tin cho hình đường tròn
x_tron = float(input("\nNhập tọa độ x của đường tròn: "))
y_tron = float(input("Nhập tọa độ y của đường tròn: "))
ban_kinh = float(input("Nhập bán kính của đường tròn: "))

duong_tron = DuongTron(x_tron, y_tron, ban_kinh)
duong_tron.display()
print(f"Diện tích đường tròn: {duong_tron.tinh_dien_tich()}")
