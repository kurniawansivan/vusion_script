import streamlit as st
import os
import subprocess

# Fungsi untuk menjalankan change_background_temp.py
def run_change_background():
    try:
        subprocess.run(['python', 'change_background_temp.py', '--config', 'config.json'], check=True)
    except subprocess.CalledProcessError as e:
        st.error(f"Error running change_background_temp.py: {e}")

# Fungsi utama untuk Streamlit app
def main():
    st.set_page_config(page_title="Hansaplast Smart System", page_icon=":guardsman:", layout="wide")
    
    # Mengatur background image dan logo
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url('assets/background_main.jpg') no-repeat center center fixed;
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Menampilkan logo dan teks
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.image("assets/hansaplast_logo.png", width=150)
        st.markdown("<h1 style='text-align: center; color: white;'>HANSAPLAST SMART SYSTEM</h1>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center; color: white;'>TOUCH TO START</h3>", unsafe_allow_html=True)
    
    # Button untuk memulai
    if st.button("Touch to Start"):
        run_change_background()

if __name__ == "__main__":
    main()
