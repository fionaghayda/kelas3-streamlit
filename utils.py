import streamlit as st

# Daftar password berdasarkan jenis halaman
passwords = {
    "nilai": "kelas3ku",
    "data": "kelas3ku",
    "galeri": "galeriku",
    "komentar": "komentarku"
}

def check_password(page="nilai"):
    def password_entered():
        if st.session_state[f"password_correct_{page}"]:
            return True
        if st.session_state[f"password_{page}"] == passwords[page]:
            st.session_state[f"password_correct_{page}"] = True
            return True
        else:
            st.session_state[f"password_correct_{page}"] = False
            return False

    if f"password_correct_{page}" not in st.session_state:
        st.session_state[f"password_correct_{page}"] = False

    if not st.session_state[f"password_correct_{page}"]:
        st.text_input("Masukkan Password", type="password", key=f"password_{page}", on_change=password_entered)
        st.stop()
