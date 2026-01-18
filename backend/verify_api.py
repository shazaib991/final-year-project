import requests
import os

# Define the URL
url = 'http://127.0.0.1:8000/api/predict/'

# Find an image to test
# We will use one from the dataset if available, or just a dummy generic path that the user should replace if not found
image_path = '../BoneFractureDataset/testing/fractured/1.jpg' 

# Check if image exists, if not try to find one dynamically
if not os.path.exists(image_path):
    # Try to find any jpg file in the dataset
    import glob
    images = glob.glob('../BoneFractureDataset/**/*.jpg', recursive=True)
    if images:
        image_path = images[0]
    else:
        print("No images found for testing.")
        exit(1)

print(f"Testing with image: {image_path}")

try:
    with open(image_path, 'rb') as f:
        files = {'image': f}
        print("Sending request to", url)
        response = requests.post(url, files=files)
    
    print("Status Code:", response.status_code)
    try:
        print("Response JSON:", response.json())
    except:
        print("Response Text:", response.text)

except Exception as e:
    print(f"Error during request: {e}")
