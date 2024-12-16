import json 

class JSONReader : 
    def __init__(self, file_path): 
        self.file_path = file_path
        self.data = None

    def read_json(self): 
        with open(self.file_path, 'r') as f : 
            self.data = json.load(f)

    def display_data(self): 
        if self.data: 
            for u in self.data : 
                print(f"name : {u['name']}, Age : {u['age']}, Address: {u['address']}")

# Su dung lop JSONReader : 
path = 'D:\DHKL17A1HN\LAB1\DATA\users.json'
reader = JSONReader(path)
reader.read_json()
reader.display_data()