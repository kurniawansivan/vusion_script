import streamlit as st
import base64

# Fungsi untuk menambahkan background image
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image:
        encoded_string = base64.b64encode(image.read())
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
            background-size: cover;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def render_home():
    st.set_page_config(page_title="Hansaplast Smart System", layout="centered")
    add_bg_from_local('assets/background_main.jpg')
    st.title("Hansaplast Smart System")
    if st.button("Touch to Start"):
        st.session_state.step = 1  # Mulai dari pertanyaan pertama
        return True
    return False

def render_question(question, options, key):
    st.markdown(f"**{question}**")
    answer = st.radio("", options, key=f"radio-{key}")
    if st.button("Next", key=f"next-{key}"):
        return answer

def render_result(result_text):
    st.markdown(f"**{result_text}**")

def get_result_background_url(answers):
    if answers == ["Outdoor activities or sports", "Often exposed to water or in a wet environment", "Wet wounds or infections caused by water"]:
        return "The suitable product is Hansaplast Plaster Aqua Protect because it protects wounds during outdoor activities in a wet environment.", "https://raw.githubusercontent.com/kurniawansivan/vusion_script/prototype/assets/left.jpg"
    elif answers == ["Indoor work or daily activities", "Occasionally exposed to water", "Open wounds needing long-term protection"]:
        return "The suitable product is Hansaplast Universal Plaster because it provides long-term protection for daily indoor activities.", "https://raw.githubusercontent.com/kurniawansivan/vusion_script/prototype/assets/middle.jpg"
    elif answers == ["Walking long distances or standing for long periods", "Rarely or almost never", "Blisters or friction on feet when walking"]:
        return "The suitable product is Hansaplast Foot Plaster because it reduces friction on feet during long walks or standing for long periods.", "https://raw.githubusercontent.com/kurniawansivan/vusion_script/prototype/assets/right.jpg"
    else:
        return None, None  # Default jika tidak ada kecocokan
