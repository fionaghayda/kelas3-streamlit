# === utils.py ===
import streamlit as st
from datetime import datetime
import pandas as pd
import os

# Konfigurasi Password
PASSWORD_NILAI = "kelas3ku"
PASSWORD_ORTU = "ortu3ku"

# Fungsi Autentikasi

def check_password(page):
    if page == "nilai_data":
        return _password_gate("password_nilai", PASSWORD_NILAI)
    elif page == "galeri_komentar":
        return _password_gate("password_ortu", PASSWORD_ORTU)
    return False

def _password_gate(key, valid_password):
    if key not in st.session_state:
        st.session_state[key] = ""

    st.session_state[key] = st.text_input("Masukkan password:", type="password", key=f"input_{key}")
    if st.session_state[key] == valid_password:
        return True
    else:
        st.warning("Password salah atau belum diisi")
        return False

# Fungsi Simpan Komentar

def simpan_komentar(nama, komentar, file_path="data/komentar.csv"):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = pd.DataFrame([[now, nama, komentar]], columns=["timestamp", "nama", "komentar"])
    if os.path.exists(file_path):
        lama = pd.read_csv(file_path)
        data = pd.concat([lama, data], ignore_index=True)
    data.to_csv(file_path, index=False)

# Fungsi Simpan Foto Galeri

def simpan_foto(file, caption, folder="data/galeri"):
    os.makedirs(folder, exist_ok=True)
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"{now}_{file.name}"
    filepath = os.path.join(folder, filename)
    with open(filepath, "wb") as f:
        f.write(file.getbuffer())

    caption_path = os.path.join(folder, f"{filename}.txt")
    with open(caption_path, "w", encoding="utf-8") as f:
        f.write(caption)

    return filepath
