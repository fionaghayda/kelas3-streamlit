import streamlit as st
import pandas as pd
import os
from datetime import datetime

# Konstanta path data
data_dir = "data"
galeri_dir = os.path.join(data_dir, "galeri")
galeri_csv = os.path.join(data_dir, "galeri.csv")
komentar_csv = os.path.join(data_dir, "komentar.csv")

# Autentikasi sederhana
PASSWORD = "kelas3ku"
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

def login():
    st.title("🔒 Halaman Khusus Guru dan Orangtua")
    pw = st.text_input("Masukkan kata sandi:", type="password")
    if st.button("Masuk"):
        if pw == PASSWORD:
            st.session_state.authenticated = True
            st.experimental_rerun()
        else:
            st.error("Kata sandi salah.")

if not st.session_state.authenticated:
    login()
    st.stop()

# UI Utama
st.set_page_config(page_title="Dashboard Kelas 3", layout="centered")
st.markdown("""
    <h1 style='text-align: center; margin-bottom: 0;'>📚 Dashboard Kelas 3</h1>
    <h4 style='text-align: center; margin-top: 0; color: gray;'>SDN Wonoplintahan I</h4>
    <hr style='border: 1px solid #eee;'>
""", unsafe_allow_html=True)

menu = st.sidebar.radio("Menu", ["Galeri", "Komentar Orangtua", "Unggah Galeri", "Berikan Komentar"])

# Galeri
if menu == "Galeri":
    st.subheader("🖼️ Galeri Kegiatan")
    if os.path.exists(galeri_csv):
        df_galeri = pd.read_csv(galeri_csv)
        for idx, row in df_galeri.iterrows():
            img_path = os.path.join(galeri_dir, row['filename'])
            if os.path.exists(img_path):
                st.image(img_path, caption=row['caption'], use_column_width=True)
            else:
                st.warning(f"Gambar tidak ditemukan: {row['filename']}")
    else:
        st.info("Belum ada foto yang ditampilkan.")

# Komentar Orangtua
elif menu == "Komentar Orangtua":
    st.subheader("💬 Komentar Orangtua")
    if os.path.exists(komentar_csv):
        df_komen = pd.read_csv(komentar_csv)
        for idx, row in df_komen.iterrows():
            with st.container():
                st.markdown(f"**🕒 {row['timestamp']}**")
                st.markdown(f"📣 {row['komentar']}")
                st.markdown("---")
    else:
        st.info("Belum ada komentar.")

# Unggah Galeri
elif menu == "Unggah Galeri":
    st.subheader("📤 Unggah Foto Baru")
    uploaded = st.file_uploader("Pilih foto", type=["png", "jpg", "jpeg"])
    caption = st.text_input("Tuliskan caption untuk foto")
    if st.button("Unggah"):
        if uploaded and caption:
            save_path = os.path.join(galeri_dir, uploaded.name)
            with open(save_path, "wb") as f:
                f.write(uploaded.getbuffer())

            new_data = pd.DataFrame([[uploaded.name, caption]], columns=["filename", "caption"])
            if os.path.exists(galeri_csv):
                old_data = pd.read_csv(galeri_csv)
                df = pd.concat([old_data, new_data], ignore_index=True)
            else:
                df = new_data
            df.to_csv(galeri_csv, index=False)
            st.success("Foto berhasil diunggah!")
        else:
            st.warning("Mohon unggah foto dan isi caption.")

# Berikan Komentar
elif menu == "Berikan Komentar":
    st.subheader("📝 Kirim Komentar untuk Guru")
    komentar = st.text_area("Tulis komentar atau usulan Anda di sini")
    if st.button("Kirim"):
        if komentar:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            new_komen = pd.DataFrame([[komentar, timestamp]], columns=["komentar", "timestamp"])
            if os.path.exists(komentar_csv):
                old_komen = pd.read_csv(komentar_csv)
                df = pd.concat([old_komen, new_komen], ignore_index=True)
            else:
                df = new_komen
            df.to_csv(komentar_csv, index=False)
            st.success("Komentar berhasil dikirim!")
        else:
            st.warning("Komentar tidak boleh kosong.")
