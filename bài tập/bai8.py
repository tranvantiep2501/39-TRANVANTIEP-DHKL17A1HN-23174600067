class Date:
    def __init__(self, day=25, month=1, year=2005): 
        self.day = day 
        self.month = month
        self.year = year

    def display(self): 
        print(f"{self.day}/{self.month}/{self.year}") # In thông tin ngày/tháng/năm
    
    def ktra_nnhuan(self):  # Kiểm tra năm nhuận
        return (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)
    
    def ngay_in_thang(self):  # Số ngày trong một tháng 
        if self.month in [1, 3, 5, 7, 8, 10, 12]: 
            return 31
        elif self.month in [4, 6, 9, 11]: 
            return 30 
        elif self.month == 2: 
            if self.ktra_nnhuan(): 
                return 29
            else: 
                return 28
    
    def next(self):  # Ngày tháng năm tiếp theo
        if self.day < self.ngay_in_thang(): 
            self.day += 1
        else: 
            self.day = 1 
            if self.month < 12: 
                self.month += 1 
            else: 
                self.month = 1 
                self.year += 1


class Employee:
    def __init__(self, ho_ten, ngay_sinh, ngay_vao_cong_ty):
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh  
        self.ngay_vao_cong_ty = ngay_vao_cong_ty  

    def display(self):
        print(f"Họ tên nhân viên: {self.ho_ten}")
        print("Ngày sinh:", end=" ")
        self.ngay_sinh.display()  # Gọi phương thức display() của lớp Date
        print("Ngày vào công ty:", end=" ")
        self.ngay_vao_cong_ty.display()  # Gọi phương thức display() của lớp Date


# Sử dụng lớp Employee
ngay_sinh = Date(15, 5, 1990)  # Ngày sinh 15/5/1990
ngay_vao_cong_ty = Date(1, 1, 2025)  # Ngày vào công ty 1/1/2015

nhan_vien = Employee("Trần Văn A", ngay_sinh, ngay_vao_cong_ty)

# In thông tin nhân viên
nhan_vien.display()
