class Stack:
    def __init__(self, size): 
        self.size = size  # Kích thước của ngăn xếp
        self.nganxep = []
        self.top = 0  # Biến đếm số phần tử trong ngăn xếp

    def isEmpty(self):   # Kiểm tra ngăn xếp có rỗng không 
        return self.top == 0
    
    def isFull(self):    # Kiểm tra ngăn xếp có đầy không
        return self.top == self.size

    def push(self, value): 
        if self.isFull():
            print("Ngăn xếp đã đầy, không thể thêm phần tử!")
        else: 
            self.nganxep.append(float(value))  # Thêm phần tử vào ngăn xếp
            self.top += 1

    def pop(self): 
        if self.isEmpty(): 
            print("Ngăn xếp rỗng, không thể lấy phần tử!")
        else : 
            self.top -= 1
            return self.nganxep.pop()  # Lấy phần tử ra khỏi ngăn xếp
    
    def print(self):
        print("Những giá trị có trên ngăn xếp là : ", self.nganxep)
#------------------------------------------------------------------

stack = Stack(5)
stack.push(1)
stack.push(2)
stack.print()