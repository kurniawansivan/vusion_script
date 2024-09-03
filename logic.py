import streamlit as st
import subprocess
from view import render_home, render_question, render_result, add_bg_from_local

def main():
    add_bg_from_local('assets/background_main.jpg')
    
    if 'step' not in st.session_state:
        st.session_state.step = 0
        st.session_state.answers = []

    if st.session_state.step == 0:
        if render_home():
            st.session_state.step = 1

    elif st.session_state.step == 1:
        question1 = "What type of activity do you do most often?"
        options1 = ["Outdoor activities or sports", "Indoor work or daily activities", "Long walks or standing for long periods"]
        answer = render_question(question1, options1, key="q1")
        if answer:
            st.session_state.answers.append(answer)
            st.session_state.step = 2

    elif st.session_state.step == 2:
        question2 = "How often do you get exposed to water or moisture during activities?"
        options2 = ["Often exposed to water or wet environments", "Occasionally exposed to water, but not too often", "Rarely or almost never exposed to water"]
        answer = render_question(question2, options2, key="q2")
        if answer:
            st.session_state.answers.append(answer)
            st.session_state.step = 3

    elif st.session_state.step == 3:
        question3 = "What is the main issue you want to avoid when using a plaster?"
        options3 = ["Wet wounds or infections caused by water", "Open wounds needing long-term protection", "Blisters or friction on the feet while walking"]
        answer = render_question(question3, options3, key="q3")
        if answer:
            st.session_state.answers.append(answer)
            st.session_state.step = 4

    elif st.session_state.step == 4:
        answers = st.session_state.answers
        
        if answers == ["Outdoor activities or sports", "Often exposed to water or wet environments", "Wet wounds or infections caused by water"]:
            result = "The recommended product is Hansaplast Plaster Aqua Protect, which protects wounds during outdoor activities in wet environments."
            image_file = 'assets/left.jpg'
            file_url = 'https://yourcdn.com/path/to/left.jpg'
        elif answers == ["Indoor work or daily activities", "Occasionally exposed to water, but not too often", "Open wounds needing long-term protection"]:
            result = "The recommended product is Hansaplast Universal Plaster, which provides long-term protection for daily indoor activities."
            image_file = 'assets/middle.jpg'
            file_url = 'https://yourcdn.com/path/to/middle.jpg'
        elif answers == ["Long walks or standing for long periods", "Rarely or almost never exposed to water", "Blisters or friction on the feet while walking"]:
            result = "The recommended product is Hansaplast Foot Plaster, which reduces friction on the feet during long walks or standing."
            image_file = 'assets/right.jpg'
            file_url = 'https://yourcdn.com/path/to/right.jpg'
        else:
            result = "No product matches your selection."
            image_file = 'assets/background_main.jpg'
            file_url = None

        render_result(result, image_file)

        if file_url:
            run_change_background(file_url)

# Fungsi untuk menjalankan change_background_temp.py
def run_change_background(new_file_url):
    original_file_url = 'https://yourcdn.com/path/to/original.jpg'
    subprocess.run([
        'python', 'change_background_temp.py',
        '--store_id', 'your_store_id',
        '--device_id', 'your_device_id',
        '--subscription_key', 'your_subscription_key',
        '--new_file_url', new_file_url,
        '--original_file_url', original_file_url
    ], check=True)
