import os
import urllib.request
import json
import time
import argparse

# Fungsi untuk membuat payload JSON
def create_payload(file_url):
    return {
        "group_id": "G1337-#FFCC00",
        "group_color": "#FFCC00",
        "layers": [
            {
                "id": "layer-1",
                "type": "image",
                "width": 1920,
                "height": 158,
                "url": file_url,
                "visible": True
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

# Fungsi untuk mengirimkan HTTP request dan mengubah background
def change_background(url, hdr, file_url):
    data = create_payload(file_url)
    
    try:
        json_data = json.dumps(data).encode("utf-8")
        req = urllib.request.Request(url, headers=hdr, data=json_data)
        req.get_method = lambda: 'POST'
        
        response = urllib.request.urlopen(req)
        print(f"Status Code: {response.getcode()}")
        response_body = response.read().decode('utf-8')
        print(response_body)
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.reason}")
    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason}")
    except Exception as e:
        print(f"Unexpected Error: {e}")

# Fungsi untuk membaca konfigurasi dari file JSON
def read_config_from_json(json_file):
    try:
        with open(json_file, 'r') as f:
            config = json.load(f)
            return config
    except Exception as e:
        raise Exception("Error reading JSON configuration file") from e

# Fungsi utama untuk eksekusi
def main(store_id, device_id, ocp_apim_subscription_key, new_file_url, original_file_url):
    url = f"https://eu-api.vusionrail.com/v1/stores/{store_id}/devices/{device_id}/background"
    hdr = create_header(ocp_apim_subscription_key)

    print("Mengubah background ke gambar baru...")
    change_background(url, hdr, new_file_url)

    time.sleep(30)  # Tunggu selama 30 detik

    print("Mengembalikan background ke gambar awal...")
    change_background(url, hdr, original_file_url)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Temporarily change device background.')
    parser.add_argument('--store_id', type=str, help='The store ID.')
    parser.add_argument('--device_id', type=str, help='The device ID.')
    parser.add_argument('--subscription_key', type=str, help='The Ocp-Apim-Subscription-Key.')
    parser.add_argument('--new_file_url', type=str, help='The URL of the new file to set as background.')
    parser.add_argument('--original_file_url', type=str, help='The URL of the original file to restore as background.')
    parser.add_argument('--config', type=str, help='Path to JSON configuration file.')

    args = parser.parse_args()

    if args.config:
        config = read_config_from_json(args.config)
        store_id = config['store_id']
        device_id = config['device_id']
        ocp_apim_subscription_key = config['subscription_key']
        new_file_url = config['file_url']
        original_file_url = config['original_file_url']
    else:
        store_id = args.store_id
        device_id = args.device_id
        ocp_apim_subscription_key = args.subscription_key
        new_file_url = args.new_file_url
        original_file_url = args.original_file_url

    if not all([store_id, device_id, ocp_apim_subscription_key, new_file_url, original_file_url]):
        raise ValueError("All parameters must be provided either through command line or JSON file")

    main(store_id, device_id, ocp_apim_subscription_key, new_file_url, original_file_url)
