import os
import urllib.request
import json
import argparse

# Fungsi untuk membuat payload JSON
def create_payload(file_url):
    return {
        "group_id": "G1337-#FFCC00",
        "group_color": "#FFCC00",
        "layers": [
            {
                "id": "layer-1",
                "type": "image",  # Bisa diganti sesuai kebutuhan (e.g., video)
                "width": 1920,
                "height": 158,
                "url": file_url,  # Gunakan URL yang diberikan
                "visible": True,
            }
        ],
    }

# Fungsi untuk membuat header request
def create_header(ocp_apim_subscription_key):
    return {
        "Content-Type": "application/json",
        "Cache-Control": "no-cache",
        "Ocp-Apim-Subscription-Key": ocp_apim_subscription_key,
    }

# Fungsi untuk mengirimkan HTTP request
def call_http(url, hdr, data):
    # Konversi data ke JSON dan kemudian ke bytes
    json_data = json.dumps(data).encode("utf-8")

    # Membuat request dengan headers dan data
    try:
        req = urllib.request.Request(url, headers=hdr, data=json_data)
    except Exception as e:
        raise Exception("Invalid URL") from e

    # Menentukan metode request sebagai 'POST'
    req.get_method = lambda: "POST"

    # Mengirim request dan mendapatkan respons
    try:
        response = urllib.request.urlopen(req)
    except Exception as e:
        raise Exception("Request failed") from e

    # Menampilkan status kode respons
    print(f"Status Code: {response.getcode()}")

    # Menampilkan body respons
    response_body = response.read().decode("utf-8")
    return response_body

# Fungsi untuk membaca konfigurasi dari file JSON
def read_config_from_json(json_file):
    try:
        with open(json_file, 'r') as f:
            config = json.load(f)
            return config
    except Exception as e:
        raise Exception("Error reading JSON configuration file") from e

# Fungsi utama untuk eksekusi
def main(store_id, device_id, ocp_apim_subscription_key, file_url):
    # URL untuk penggantian background
    url = f"https://eu-api.vusionrail.com/v1/stores/{store_id}/devices/{device_id}/background"

    # Membuat payload dan header
    data = create_payload(file_url)
    hdr = create_header(ocp_apim_subscription_key)

    # Mengirimkan request dan mendapatkan respons
    response = call_http(url, hdr, data)
    print(f"Response: {response}")

if __name__ == "__main__":
    # Menggunakan argparse untuk mengambil input dari command line atau JSON file
    parser = argparse.ArgumentParser(description='Change device background.')
    parser.add_argument('--store_id', type=str, help='The store ID.')
    parser.add_argument('--device_id', type=str, help='The device ID.')
    parser.add_argument('--subscription_key', type=str, help='The Ocp-Apim-Subscription-Key.')
    parser.add_argument('--file_url', type=str, help='The URL of the file to set as background.')
    parser.add_argument('--config', type=str, help='Path to JSON configuration file.')

    # Parsing arguments
    args = parser.parse_args()

    # Jika file JSON diberikan, gunakan itu untuk konfigurasi
    if args.config:
        config = read_config_from_json(args.config)
        store_id = config['store_id']
        device_id = config['device_id']
        ocp_apim_subscription_key = config['subscription_key']
        file_url = config['file_url']
    else:
        # Jika tidak ada JSON file, gunakan args dari command line
        store_id = args.store_id
        device_id = args.device_id
        ocp_apim_subscription_key = args.subscription_key
        file_url = args.file_url

    # Memastikan semua variabel diisi
    if not all([store_id, device_id, ocp_apim_subscription_key, file_url]):
        raise ValueError("All parameters must be provided either through command line or JSON file")

    # Menjalankan fungsi utama
    main(store_id, device_id, ocp_apim_subscription_key, file_url)
