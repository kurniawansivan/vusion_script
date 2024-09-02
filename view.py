import streamlit as st

def render_view():
    st.set_page_config(page_title="Hansaplast Smart System", page_icon=":guardsman:", layout="wide")
    
    # Mengatur background image dan logo
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url('assets/background_main.jpg');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        .center-content {{
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            flex-direction: column;
            text-align: center;
        }}
        .logo {{
            width: 300px;
            margin-bottom: 20px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Mengatur layout konten di tengah layar
    st.markdown('<div class="center-content">', unsafe_allow_html=True)
    st.image("assets/hansaplast_logo.png", use_column_width=False, width=300)
    st.markdown("<h1 style='color: white;'>HANSAPLAST SMART SYSTEM</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: white;'>TOUCH TO START</h3>", unsafe_allow_html=True)
    
    # Button untuk memulai
    if st.button("Touch to Start"):
        return True  # Mengembalikan True jika tombol ditekan
    
    st.markdown('</div>', unsafe_allow_html=True)
    return False  # Mengembalikan False jika tombol tidak ditekan
