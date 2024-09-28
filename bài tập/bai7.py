class Date:
    def __init__(self, day=25, month=01, year=2005): 
        self.day = day 
        self.month = month
        self.year = year

    def Display(self): 
        print(f"{self.day}/{self.month}/{self.year}") # in thông tin ngày/tháng/năm
    
    def ktra_nnhuan(self): # ktra năm nhuận 
        return (self.nam % 4 == 0 and self.nam % 100 != 0) or (self.nam % 400 == 0)
    
    def ngay_in_thang(self): # số ngày trong một tháng 
        if self.thang in [1, 3, 5, 7, 8, 10, 12]: 
            return 31
        elif self.thang in [4, 6, 9, 11]: 
            return 30 
        elif self.thang == 2 : 
            if self.ktra_nnhuan(): 
                return 29
            else: 
                return 28
    
    def Next(self): # ngày tháng năm tiếp 
        if self.ngay < self.ngay_in_thang(): 
            self.ngay += 1
        else : 
            self.ngay == 1 
            if self.thang < 12 : 
                self.thang += 1 
            else: 
                self.thang == 1 
                self.nam += 1
#-----------------------------------------------------------------
