# File: utils.py
import streamlit as st
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Daftar password untuk setiap halaman privat
PASSWORDS = {
    "nilai": hash_password("kelas3ku"),
    "data": hash_password("kelas3ku"),
    "komentar": hash_password("ortu3ku"),
    "galeri": hash_password("ortu3ku"),
}

# Fungsi pengecekan password berdasarkan halaman
@st.cache_data(show_spinner=False)
def check_password(page="data"):
    if f"_authenticated_{page}" not in st.session_state:
        st.session_state[f"_authenticated_{page}"] = False

    if not st.session_state[f"_authenticated_{page}"]:
        with st.form(f"Login_{page}"):
            st.write(f"🔒 Halaman ini dilindungi. Masukkan password untuk mengakses.")
            password = st.text_input("Password", type="password")
            submitted = st.form_submit_button("Login")
            if submitted:
                if hash_password(password) == PASSWORDS.get(page):
                    st.session_state[f"_authenticated_{page}"] = True
                else:
                    st.error("Password salah.")
    return st.session_state[f"_authenticated_{page}"]
