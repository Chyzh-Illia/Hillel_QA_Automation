import requests

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'

params = {
    'sol': 1000,
    'camera': 'fhaz',
    'api_key': 'DEMO_KEY'
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    photos = data.get('photos', [])

    if not photos:
        print("No photos found for the given parameters.")
    else:
        for idx, photo in enumerate(photos, start=1):
            img_url = photo.get('img_src')
            if img_url:
                try:
                    img_data = requests.get(img_url).content
                    file_name = f"mars_photo{idx}.jpg"

                    with open(file_name, 'wb') as img_file:
                        img_file.write(img_data)

                    print(f"Saved: {file_name}")
                except Exception as e:
                    print(f"Failed to save photo {idx}: {e}")
else:
    print(f"Failed to fetch data from NASA API. Status code: {response.status_code}")
