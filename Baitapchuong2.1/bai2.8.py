import json

data_object = {
    "name":"Trần Văn A",
    "age":30,
    "chuc_vu": "giám đốc"
}

data_string = json.dumps(data_object, ensure_ascii=False)

print(data_string)