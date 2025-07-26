import streamlit as st
import pandas as pd
import os

def show_komentar_page():
    st.header("💬 Komentar dan Usulan Orang Tua")

    komentar_file = "data/komentar.csv"

    nama = st.text_input("Nama Orang Tua")
    komentar = st.text_area("Komentar atau Usulan")

    if st.button("Kirim Komentar"):
        if nama and komentar:
            df = pd.DataFrame([[pd.Timestamp.now(), nama, komentar]], columns=["timestamp", "nama", "komentar"])
            if os.path.exists(komentar_file):
                df.to_csv(komentar_file, mode='a', index=False, header=False)
            else:
                df.to_csv(komentar_file, index=False)
            st.success("Komentar berhasil dikirim!")
        else:
            st.warning("Nama dan komentar harus diisi.")

    # Tampilkan komentar yang sudah masuk
    if os.path.exists(komentar_file):
        st.markdown("### Komentar Sebelumnya:")
        df = pd.read_csv(komentar_file)
        for _, row in df.iterrows():
            st.markdown(f"🕒 {row['timestamp']}  
**{row['nama']}**: {row['komentar']}")
