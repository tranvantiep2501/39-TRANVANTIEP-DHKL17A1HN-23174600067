import json 
data_python = {
    "name":"Trần Văn A",
    "age": 30,
    "chuc_vu":"giám đốc",
    "address":"Hà Nội"
}

data_json = json.dumps(data_python, sort_keys=True, indent=4, ensure_ascii=False)

print(data_json)