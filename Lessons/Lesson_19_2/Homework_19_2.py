import requests

BASE_URL = "http://127.0.0.1:8080"
IMAGE_PATH = "example.jpg"  # Specify the path to your image

upload_url = f"{BASE_URL}/upload"
files = {'image': open(IMAGE_PATH, 'rb')}
response = requests.post(upload_url, files=files)
files['image'].close()

if response.status_code == 201:
    image_url = response.json().get("image_url")
    print(f"Image successfully uploaded: {image_url}")
else:
    print(f"Upload error: {response.text}")
    exit()

filename = image_url.split("/")[-1]
get_url = f"{BASE_URL}/image/{filename}"
headers = {'Content-Type': 'text'}
response = requests.get(get_url, headers=headers)

if response.status_code == 200:
    print(f"Image URL: {response.json().get('image_url')}")
else:
    print(f"Error retrieving URL: {response.text}")

delete_url = f"{BASE_URL}/delete/{filename}"
response = requests.delete(delete_url)

if response.status_code == 200:
    print(f"Image {filename} successfully deleted")
else:
    print(f"Deletion error: {response.text}")
