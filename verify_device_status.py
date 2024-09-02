import os
import requests

# Ambil data dari environment variables (GitHub Secrets)
storeId = os.getenv('STORE_ID')
deviceId = os.getenv('DEVICE_ID')
Ocp_Apim_Subscription_Key = os.getenv('OCP_APIM_SUBSCRIPTION_KEY')

# URL untuk mendapatkan status perangkat
url = f"https://eu-api.vusionrail.com/v1/stores/{storeId}/devices/{deviceId}"

# Header yang diperlukan
headers = {
    "Ocp-Apim-Subscription-Key": Ocp_Apim_Subscription_Key,
    "Content-Type": "application/json"
}

# Kirim permintaan GET untuk verifikasi status perangkat
response = requests.get(url, headers=headers)

# Tampilkan hasilnya
print(f"Status Code: {response.status_code}")
print(f"Response: {response.json()}")
