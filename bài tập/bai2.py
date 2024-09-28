class describe_student:
    def __init__(self, ten=0, diem_toan=0, diem_ly=0, diem_hoa=0):
        self.ten = ten 
        self.diem_toan = diem_toan
        self.diem_ly = diem_ly
        self.diem_hoa = diem_hoa
    
    def nhap(self): 
        while True: 
            try: 
                self.ten = input("Nhập tên của thí sinh : ")
                self.diem_toan = float(input("Nhập điểm toán của thí sinh : "))
                self.diem_ly = float(input("Nhập điểm lý của thí sinh : "))
                self.diem_hoa = float(input("Nhập điểm hóa của thí sinh : "))
                break
            except ValueError:
                print("Vui lòng nhập lại !!!")
    
    def tong_diem(self):
        return self.diem_toan + self.diem_hoa + self.diem_ly
    
    def in_ttin(self):
        print("Tổng điểm của thí sinh là  :", self.tong_diem())
#----------------------------------------------------
thi_sinh = describe_student()
thi_sinh.nhap()
thi_sinh.in_ttin()
#---------------------------------------------------
list_ttuyen = []
if thi_sinh.tong_diem() >= 20 : 
    list_ttuyen.append(thi_sinh.ten)
else: 
    print("thí sinh này đã bị trượt !!!")
#------------------------------------
print("Những thí sinh trúng tuyển là : ")
for i in list_ttuyen: 
    print(i)