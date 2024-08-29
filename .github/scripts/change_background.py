import os
import requests

# Ambil data dari environment variables (GitHub Actions Variables)
storeId = os.getenv('STORE_ID')
deviceId = os.getenv('DEVICE_ID')
Ocp_Apim_Subscription_Key = os.getenv('OCP_APIM_SUBSCRIPTION_KEY')
file_url = os.getenv('FILE_URL')  # Ambil URL dari GitHub Actions Variable

# URL untuk penggantian background
url = f"https://eu-api.vusionrail.com/v1/stores/{storeId}/devices/{deviceId}/background"

# Header yang diperlukan
headers = {
    "Ocp-Apim-Subscription-Key": Ocp_Apim_Subscription_Key,
    "Content-Type": "application/json"
}

# Body untuk penggantian background
data = {
    "groupId": "G1337-#FFCC00",
    "groupColor": "#FFCC00",
    "layers": [
        {
            "id": "layer-1",
            "type": "image",  # Bisa diganti sesuai kebutuhan (e.g., video)
            "width": 1920,
            "height": 158,
            "url": file_url,  # Gunakan URL dari GitHub Actions Variable
            "visible": True
        }
    ]
}

# Kirim permintaan POST untuk mengganti background
response = requests.post(url, json=data, headers=headers)

# Tampilkan hasilnya
print(f"Status Code: {response.status_code}")
print(f"Response: {response.json()}")
