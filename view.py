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

def render_view():
    st.set_page_config(page_title="Hansaplast Smart System", layout="centered")
    
    # Tambahkan gambar latar belakang
    add_bg_from_local('assets/background_main.jpg')
    
    # Mengatur semua konten di tengah layar
    st.markdown(
        """
        <style>
        .block-container {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Menampilkan judul
    st.title("Hansaplast Smart System")
    
    # Button untuk memulai
    if st.button("Touch to Start"):
        return True  # Mengembalikan True jika tombol ditekan

    return False  # Mengembalikan False jika tombol tidak ditekan
