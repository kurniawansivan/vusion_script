import os
import urllib.request
import json
import time
import argparse

# Fungsi untuk membuat payload JSON dengan cacheId
def create_payload(file_url, cache_id):
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
                "cacheId": cache_id,  # Menambahkan cacheId
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
def change_background(url, hdr, file_url, cache_id):
    data = create_payload(file_url, cache_id)
    
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
def main(store_id, device_id, ocp_apim_subscription_key, selected_file_url, cache_id, background_url):
    url = f"https://eu-api.vusionrail.com/v1/stores/{store_id}/devices/{device_id}/background"
    hdr = create_header(ocp_apim_subscription_key)

    print("Mengubah background ke gambar baru...")
    change_background(url, hdr, selected_file_url, cache_id)

    time.sleep(30)  # Tunggu selama 30 detik

    print("Mengembalikan background ke gambar awal...")
    change_background(url, hdr, background_url, None)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Temporarily change device background.')
    parser.add_argument('--store_id', type=str, help='The store ID.')
    parser.add_argument('--device_id', type=str, help='The device ID.')
    parser.add_argument('--subscription_key', type=str, help='The Ocp-Apim-Subscription-Key.')
    parser.add_argument('--selected_file_url', type=str, help='The URL of the selected file to set as background.')
    parser.add_argument('--cache_id', type=str, help='The cache ID of the selected file.')
    parser.add_argument('--background_url', type=str, help='The URL of the background to restore.')

    args = parser.parse_args()

    config = read_config_from_json('config.json')
    store_id = config.get('store_id', args.store_id)
    device_id = config.get('device_id', args.device_id)
    ocp_apim_subscription_key = config.get('subscription_key', args.subscription_key)
    background_url = config.get('background_url', args.background_url)
    selected_file_url = args.selected_file_url
    cache_id = args.cache_id

    if not all([store_id, device_id, ocp_apim_subscription_key, selected_file_url, background_url]):
        raise ValueError("All parameters must be provided either through command line or JSON file")

    main(store_id, device_id, ocp_apim_subscription_key, selected_file_url, cache_id, background_url)
