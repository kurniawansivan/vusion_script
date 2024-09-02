import os
import urllib.request
import json
import time  # Import modul time untuk mengatur delay

# Ambil data dari environment variables (GitHub Actions Variables dan Secrets)
storeId = os.getenv('STORE_ID')
deviceId = os.getenv('DEVICE_ID')
Ocp_Apim_Subscription_Key = os.getenv('OCP_APIM_SUBSCRIPTION_KEY')
new_file_url = os.getenv('FILE_URL')  # Ambil URL gambar baru dari GitHub Actions Variable
original_file_url = os.getenv('ORIGINAL_FILE_URL')  # Ambil URL gambar awal dari GitHub Actions Variable

# URL untuk penggantian background
url = f"https://eu-api.vusionrail.com/v1/stores/{storeId}/devices/{deviceId}/background"

# Header yang diperlukan
hdr = {
    'Content-Type': 'application/json',
    'Cache-Control': 'no-cache',
    'Ocp-Apim-Subscription-Key': Ocp_Apim_Subscription_Key,
}

def change_background(file_url):
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
                "url": file_url,  # Gunakan URL yang diberikan
                "visible": True
            }
        ]
    }

    try:
        # Konversi data ke JSON dan kemudian ke bytes
        json_data = json.dumps(data).encode("utf-8")
        
        # Membuat request dengan headers dan data
        req = urllib.request.Request(url, headers=hdr, data=json_data)
        
        # Menentukan metode request sebagai 'POST'
        req.get_method = lambda: 'POST'
        
        # Mengirim request dan mendapatkan respons
        response = urllib.request.urlopen(req)
        
        # Menampilkan status kode respons
        print(f"Status Code: {response.getcode()}")
        
        # Menampilkan body respons
        response_body = response.read().decode('utf-8')
        print(response_body)

    except Exception as e:
        print(f"Error: {e}")

# Set background ke gambar baru
print("Mengubah background ke gambar baru...")
change_background(new_file_url)

# Tunggu selama 1 menit
time.sleep(30)

# Kembalikan background ke gambar awal
print("Mengembalikan background ke gambar awal...")
change_background(original_file_url)
