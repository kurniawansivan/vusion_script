import os
import requests
import argparse
import json

# Fungsi untuk membuat header request
def create_header(ocp_apim_subscription_key):
    return {
        "Ocp-Apim-Subscription-Key": ocp_apim_subscription_key,
        "Content-Type": "application/json"
    }

# Fungsi untuk mendapatkan status perangkat
def get_device_status(url, headers):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Akan memunculkan error jika status code bukan 200
        return response.json(), response.status_code
    except requests.exceptions.RequestException as e:
        raise Exception(f"Request failed: {e}")

# Fungsi untuk membaca konfigurasi dari file JSON
def read_config_from_json(json_file):
    try:
        with open(json_file, 'r') as f:
            config = json.load(f)
            return config
    except Exception as e:
        raise Exception("Error reading JSON configuration file") from e

# Fungsi utama untuk eksekusi
def main(store_id, device_id, ocp_apim_subscription_key):
    # URL untuk mendapatkan status perangkat
    url = f"https://eu-api.vusionrail.com/v1/stores/{store_id}/devices/{device_id}"

    # Membuat header
    headers = create_header(ocp_apim_subscription_key)

    # Mendapatkan status perangkat
    response, status_code = get_device_status(url, headers)
    
    # Tampilkan hasilnya
    print(f"Status Code: {status_code}")
    print(f"Response: {json.dumps(response, indent=4)}")

if __name__ == "__main__":
    # Menggunakan argparse untuk mengambil input dari command line atau JSON file
    parser = argparse.ArgumentParser(description='Verify device status.')
    parser.add_argument('--store_id', type=str, help='The store ID.')
    parser.add_argument('--device_id', type=str, help='The device ID.')
    parser.add_argument('--subscription_key', type=str, help='The Ocp-Apim-Subscription-Key.')
    parser.add_argument('--config', type=str, help='Path to JSON configuration file.')

    # Parsing arguments
    args = parser.parse_args()

    # Jika file JSON diberikan, gunakan itu untuk konfigurasi
    if args.config:
        config = read_config_from_json(args.config)
        store_id = config['store_id']
        device_id = config['device_id']
        ocp_apim_subscription_key = config['subscription_key']
    else:
        # Jika tidak ada JSON file, gunakan args dari command line
        store_id = args.store_id
        device_id = args.device_id
        ocp_apim_subscription_key = args.subscription_key

    # Memastikan semua variabel diisi
    if not all([store_id, device_id, ocp_apim_subscription_key]):
        raise ValueError("All parameters must be provided either through command line or JSON file")

    # Menjalankan fungsi utama
    main(store_id, device_id, ocp_apim_subscription_key)
