from view import render_home, render_question, render_result
import streamlit as st
import subprocess
import json

# Fungsi untuk membaca konfigurasi dari file JSON
def read_config_from_json(json_file):
    try:
        with open(json_file, 'r') as f:
            config = json.load(f)
            return config
    except Exception as e:
        raise Exception("Error reading JSON configuration file") from e

def get_result_background_url(answers):
    config = read_config_from_json('config.json')
    
    if answers == ["Outdoor activities or sports", "Often exposed to water or in a wet environment", "Wet wounds or infections caused by water"]:
        return "The suitable product is Hansaplast Plaster Aqua Protect because it protects wounds during outdoor activities in wet environments.", config['hansaplast_waterproof_url'], config['hansaplast_waterproof_cache_id']
    elif answers == ["Indoor work or daily activities", "Occasionally exposed to water", "Open wounds needing long-term protection"]:
        return "The suitable product is Hansaplast Universal Plaster because it provides long-term protection for daily indoor activities.", config['hansaplast_universal_url'], config['hansaplast_universal_cache_id']
    elif answers == ["Walking long distances or standing for long periods", "Rarely or almost never", "Blisters or friction on feet when walking"]:
        return "The suitable product is Hansaplast Foot Plaster because it reduces friction on feet during long walks or standing.", config['hansaplast_foot_url'], config['hansaplast_foot_cache_id']
    else:
        return None, None, None

def main():
    if 'step' not in st.session_state:
        st.session_state.step = 0  # Inisialisasi step jika belum ada

    questions = [
        "What type of activity do you do most often?",
        "How often are you exposed to water or moisture during activities?",
        "What is the main issue you want to avoid when using a plaster?"
    ]
    options = [
        ["Outdoor activities or sports", "Indoor work or daily activities", "Walking long distances or standing for long periods"],
        ["Often exposed to water or in a wet environment", "Occasionally exposed to water", "Rarely or almost never"],
        ["Wet wounds or infections caused by water", "Open wounds needing long-term protection", "Blisters or friction on feet when walking"]
    ]

    # Tampilkan halaman utama
    if st.session_state.step == 0:
        render_home()

    # Tampilkan pertanyaan satu per satu
    elif st.session_state.step in [1, 2, 3]:
        answer = render_question(questions[st.session_state.step - 1], options[st.session_state.step - 1], key=st.session_state.step)
        if answer:
            st.session_state[f"answer_{st.session_state.step}"] = answer
            st.session_state.step += 1

    # Tampilkan hasil setelah semua pertanyaan dijawab
    elif st.session_state.step == 4:
        answers = [st.session_state.get(f"answer_{i}") for i in range(1, 4)]
        result_text, new_background_url, cache_id = get_result_background_url(answers)
        if result_text and new_background_url:
            render_result(result_text)
            subprocess.run(['python', 'change_background_temp.py', '--selected_file_url', new_background_url, '--cache_id', cache_id])
        else:
            st.error("No suitable product found for the given answers.")
