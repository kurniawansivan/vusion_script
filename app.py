import streamlit as st
import subprocess
from view import render_view

# Fungsi untuk menjalankan change_background_temp.py
def run_change_background():
    try:
        subprocess.run(['python', 'change_background_temp.py', '--config', 'config.json'], check=True)
    except subprocess.CalledProcessError as e:
        st.error(f"Error running change_background_temp.py: {e}")

def main():
    if render_view():
        run_change_background()

if __name__ == "__main__":
    main()
