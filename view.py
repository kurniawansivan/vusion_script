import streamlit as st
import base64
import time

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
    st.title("Hansaplast Smart System")
    if st.button("Touch to Start"):
        return True
    return False

def render_question(question, options, key):
    st.markdown(f"### <span style='color:white;'>{question}</span>", unsafe_allow_html=True)
    selected = st.radio("", options, key=key)
    if st.button("Next", key=f"next-{key}"):
        return selected
    return None

def render_result(result, image_file):
    st.markdown(f"## <span style='color:white;'>{result}</span>", unsafe_allow_html=True)
    add_bg_from_local(image_file)
    time.sleep(30)  # Tampilkan background baru selama 30 detik
