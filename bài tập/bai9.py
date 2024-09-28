# Lớp Đa Giác
class DaGiac:
    def __init__(self, so_canh, do_dai_cac_canh):
        self.so_canh = so_canh
        self.do_dai_cac_canh = do_dai_cac_canh  # List chứa độ dài các cạnh

    def tinh_chu_vi(self):
        return sum(self.do_dai_cac_canh)  # Tổng độ dài các cạnh

# Lớp Hình Bình Hành kế thừa từ Đa Giác
class HinhBinhHanh(DaGiac):
    def __init__(self, canh_day, canh_ben, chieu_cao):
        # Hình bình hành có 4 cạnh: 2 cạnh đáy, 2 cạnh bên
        super().__init__(4, [canh_day, canh_ben, canh_day, canh_ben])
        self.canh_day = canh_day
        self.canh_ben = canh_ben
        self.chieu_cao = chieu_cao

    def tinh_dien_tich(self):
        return self.canh_day * self.chieu_cao  # Diện tích = đáy * chiều cao

# Lớp Hình Chữ Nhật kế thừa từ Hình Bình Hành
class HinhChuNhat(HinhBinhHanh):
    def __init__(self, chieu_dai, chieu_rong):
        # Hình chữ nhật cũng là hình bình hành với chiều cao = chiều rộng
        super().__init__(chieu_dai, chieu_rong, chieu_rong)
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    def tinh_dien_tich(self):
        return self.chieu_dai * self.chieu_rong  # Diện tích = dài * rộng

# Lớp Hình Vuông kế thừa từ Hình Chữ Nhật
class HinhVuong(HinhChuNhat):
    def __init__(self, canh):
        # Hình vuông là một trường hợp đặc biệt của hình chữ nhật với chiều dài = chiều rộng
        super().__init__(canh, canh)
        self.canh = canh

    def tinh_dien_tich(self):
        return self.canh ** 2  # Diện tích = cạnh^2

# Nhập dữ liệu và tính toán

# Hình bình hành
canh_day = float(input("Nhập chiều dài cạnh đáy của hình bình hành: "))
canh_ben = float(input("Nhập chiều dài cạnh bên của hình bình hành: "))
chieu_cao = float(input("Nhập chiều cao của hình bình hành: "))
hinh_binh_hanh = HinhBinhHanh(canh_day, canh_ben, chieu_cao)
print(f"Chu vi hình bình hành: {hinh_binh_hanh.tinh_chu_vi()}")
print(f"Diện tích hình bình hành: {hinh_binh_hanh.tinh_dien_tich()}")

# Hình chữ nhật
chieu_dai = float(input("\nNhập chiều dài của hình chữ nhật: "))
chieu_rong = float(input("Nhập chiều rộng của hình chữ nhật: "))
hinh_chu_nhat = HinhChuNhat(chieu_dai, chieu_rong)
print(f"Chu vi hình chữ nhật: {hinh_chu_nhat.tinh_chu_vi()}")
print(f"Diện tích hình chữ nhật: {hinh_chu_nhat.tinh_dien_tich()}")

# Hình vuông
canh_vuong = float(input("\nNhập cạnh của hình vuông: "))
hinh_vuong = HinhVuong(canh_vuong)
print(f"Chu vi hình vuông: {hinh_vuong.tinh_chu_vi()}")
print(f"Diện tích hình vuông: {hinh_vuong.tinh_dien_tich()}")
