from view import render_home, render_question, render_result, add_bg_from_local
import streamlit as st
import subprocess

def get_result_background_url(answers):
    if answers == ["Outdoor activities or sports", "Often exposed to water or in a wet environment", "Wet wounds or infections caused by water"]:
        return "The suitable product is Hansaplast Plaster Aqua Protect because it protects wounds during outdoor activities in wet environments.", "https://raw.githubusercontent.com/kurniawansivan/vusion_script/prototype/assets/left.jpg"
    elif answers == ["Indoor work or daily activities", "Occasionally exposed to water", "Open wounds needing long-term protection"]:
        return "The suitable product is Hansaplast Universal Plaster because it provides long-term protection for daily indoor activities.", "https://raw.githubusercontent.com/kurniawansivan/vusion_script/prototype/assets/middle.jpg"
    elif answers == ["Walking long distances or standing for long periods", "Rarely or almost never", "Blisters or friction on feet when walking"]:
        return "The suitable product is Hansaplast Foot Plaster because it reduces friction on feet during long walks or standing.", "https://raw.githubusercontent.com/kurniawansivan/vusion_script/prototype/assets/right.jpg"
    else:
        return None, None

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
        result_text, new_background_url = get_result_background_url(answers)
        if result_text and new_background_url:
            render_result(result_text)
            subprocess.run(['python', 'change_background_temp.py', '--selected_file_url', new_background_url])
        else:
            st.error("No suitable product found for the given answers.")
