
import urllib.request
import json

# Địa chỉ API từ đề bài
url = 'https://jsonplaceholder.typicode.com/comments?postId=1'

try:
    # Gửi yêu cầu GET tới API
    with urllib.request.urlopen(url) as response:
        data = response.read()  # Đọc dữ liệu từ phản hồi
        comments = json.loads(data)  # Chuyển đổi từ JSON

    # Hiển thị danh sách các bài post với postId = 1
    print(f"Danh sách các bài post với postId = 1:\n")

    # Hiển thị thông tin của 3 bài post đầu tiên
    for i, comment in enumerate(comments[:3], 1):  # Chỉ hiển thị 3 bài đầu tiên
        print(f"Bài post {i}:")
        print(f"ID: {comment['id']}")
        print(f"Name: {comment['name']}")
        print(f"Email: {comment['email']}")
        print(f"Body: {comment['body']}")
        print("-" * 50)

except urllib.error.URLError as e:
    print(f"Lỗi khi kết nối tới API: {e}")
