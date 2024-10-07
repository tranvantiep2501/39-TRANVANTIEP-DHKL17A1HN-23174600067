import json

data_json = '{"name":"Trần Văn A", "age":30, "chuc_vu": "giám đốc"}'

data_python = json.loads(data_json)

print(data_python)