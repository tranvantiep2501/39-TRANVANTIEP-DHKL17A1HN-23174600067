class HCN:
    def __init__(self, chieu_dai = 0, chieu_rong = 0):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong
    
    def nhap(self):
        while True : 
            try : 
                self.chieu_dai = float(input("Nhập chiều dài của hình chữ nhật : "))
                self.chieu_rong = float(input("Nhập chiều rộng của hình chữ nhật : "))
                break
            except ValueError: 
                print("Vui lòng nhập lại !!!")
    
    def chu_vi(self):
        return (self.chieu_dai + self.chieu_rong) * 2

    def dien_tich(self):
        return self.chieu_dai * self.chieu_rong
    
    def in_thtin(self):
        print("chu vi của hình chữ nhật là : ", self.chu_vi())
        print("diện tích của hình chữ nhật là : ", self.dien_tich())
#-------------------------------------------------------------
ttin_hcn = HCN()
ttin_hcn.nhap()
ttin_hcn.in_thtin()