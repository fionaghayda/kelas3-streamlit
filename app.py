import streamlit as st
import pandas as pd
import os
from utils import check_password, check_guest_password

st.set_page_config(page_title="Dokumentasi Akademik Kelas 3", layout="centered")
st.title("📘 Dokumentasi Akademik Kelas 3")
st.markdown("SDN Wonoplintahan 1 - Kecamatan Prambon, Sidoarjo")
st.markdown("🧑‍🏫 Oleh: Ibu RINI KUS ENDANG, S.Pd")

MENU_OPTIONS = ["Data Siswa", "Nilai Siswa", "Galeri", "Komentar Orang Tua"]

menu = st.sidebar.selectbox("📁 Pilih Halaman", MENU_OPTIONS)

if menu in ["Data Siswa", "Nilai Siswa"]:
    if not check_password():
        st.stop()

    if menu == "Data Siswa":
        st.header("👨‍🎓 Data Siswa")
        df_siswa = pd.read_csv("data/siswa.csv")
        st.dataframe(df_siswa, use_container_width=True)

    elif menu == "Nilai Siswa":
        st.header("📊 Nilai Siswa")
        df_nilai = pd.read_csv("data/nilai.csv")
        st.dataframe(df_nilai, use_container_width=True)

elif menu in ["Galeri", "Komentar Orang Tua"]:
    if not check_guest_password():
        st.stop()

    if menu == "Galeri":
        st.header("🖼️ Galeri Kegiatan")
        galeri_file = "data/galeri.csv"

        if os.path.exists(galeri_file):
            df_galeri = pd.read_csv(galeri_file)
        else:
            df_galeri = pd.DataFrame(columns=["file", "caption"])

        # Tampilkan galeri
        for idx, row in df_galeri.iterrows():
            st.image(f"data/galeri/{row['file']}", width=300)
            new_caption = st.text_input(f"Edit Caption ({row['file']})", value=row['caption'], key=f"cap{idx}")
            if new_caption != row['caption']:
                df_galeri.at[idx, 'caption'] = new_caption

            if st.button(f"Hapus Gambar {row['file']}", key=f"hapus{idx}"):
                try:
                    os.remove(f"data/galeri/{row['file']}")
                except:
                    pass
                df_galeri = df_galeri.drop(index=idx).reset_index(drop=True)
                df_galeri.to_csv(galeri_file, index=False)
                st.experimental_rerun()

        df_galeri.to_csv(galeri_file, index=False)

    elif menu == "Komentar Orang Tua":
        st.header("💬 Komentar dan Usulan Orang Tua")

        komentar_file = "data/komentar.csv"
        if os.path.exists(komentar_file):
            df_komentar = pd.read_csv(komentar_file)
        else:
            df_komentar = pd.DataFrame(columns=["timestamp", "nama", "komentar"])

        with st.form("form_komentar"):
            nama = st.text_input("Nama Orang Tua")
            komentar = st.text_area("Komentar atau Usulan")
            submitted = st.form_submit_button("Kirim")
            if submitted and nama and komentar:
                new_row = pd.DataFrame({"timestamp": [pd.Timestamp.now()], "nama": [nama], "komentar": [komentar]})
                df_komentar = pd.concat([new_row, df_komentar], ignore_index=True)
                df_komentar.to_csv(komentar_file, index=False)
                st.success("Komentar berhasil dikirim!")

        st.markdown("🗒️ **Komentar Terkirim:**")
        for idx, row in df_komentar.iterrows():
            st.write(f"🕒 {row['timestamp']} - ✍️ {row['nama']}: {row['komentar']}")
            if st.button(f"Hapus Komentar {idx}", key=f"hapuskomen{idx}"):
                df_komentar = df_komentar.drop(index=idx).reset_index(drop=True)
                df_komentar.to_csv(komentar_file, index=False)
                st.experimental_rerun()
