import urllib.request
import json

# URL API để lấy danh sách các bài post
url = "https://jsonplaceholder.typicode.com/posts"

try:
    # Gửi yêu cầu GET tới API
    with urllib.request.urlopen(url) as response:
        data = response.read()  # Đọc dữ liệu từ phản hồi
        posts = json.loads(data)  # Chuyển đổi từ JSON

    # Hiển thị tổng số bài post
    print(f"Tổng số bài post: {len(posts)}\n")

    # Hiển thị danh sách tối đa 5 bài post
    for post in posts[:5]:  # Chỉ hiển thị 5 bài đầu
        print(f"User ID: {post['userId']}")
        print(f"ID: {post['id']}")
        print(f"Title: {post['title']}")
        print(f"Body: {post['body']}")
        print("-" * 40)

except urllib.error.URLError as e:
    print(f"Lỗi khi lấy dữ liệu từ API: {e}")
