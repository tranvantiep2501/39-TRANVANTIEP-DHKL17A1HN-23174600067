class PS: 
    def __init__(self, tu_so=0, mau_so=0):
        self.tu_so = tu_so
        self.mau_so = mau_so
    
    def ktra_hle(self):
        return self.mau_so != 0 

    def nhap(self):
        while True : 
            try : 
                self.tu_so = int(input("Nhập tử số của phân số : "))
                self.mau_so = int(input("Nhập mẫu số của phân số : "))
                if self.ktra_hle() : 
                    break
                else: 
                    print("Vui lòng nhập lại mẫu số !!!")
            except ValueError: 
                print("Giá trị không hợp lệ !!!")
    
    def in_ps(self):
        print("Phân số là : ", self.tu_so, "/", self.mau_so)
#----------------------------------------------
phan_so = PS()
phan_so.nhap()
phan_so.in_ps()