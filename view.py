import streamlit as st

def render_view():
    st.set_page_config(page_title="Hansaplast Smart System", layout="centered")
    
    # Menampilkan judul
    st.title("Hansaplast Smart System")
    
    # Button untuk memulai
    if st.button("Touch to Start"):
        return True  # Mengembalikan True jika tombol ditekan

    return False  # Mengembalikan False jika tombol tidak ditekan
