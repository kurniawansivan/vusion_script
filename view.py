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
    return None

def render_result(result_text):
    st.markdown(f"**{result_text}**")
    st.button("Back to Home", on_click=lambda: st.session_state.update(step=0))
