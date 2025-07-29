import streamlit as st
import pandas as pd
from datetime import datetime
import os

def show_komentar_page(user):
    st.header("💬 Komentar Orang Tua")
    file = "data/komentar.csv"

    komentar = st.text_area("Tulis komentar atau usulan")
    if st.button("Kirim Komentar"):
        if komentar:
            waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(file,"a") as f:
                f.write(f"{user},{komentar},{waktu}\n")
            st.success("✅ Komentar terkirim")
            st.experimental_rerun()

    if os.path.exists(file):
        df = pd.read_csv(file, names=["nama","komentar","waktu"])
        for _, row in df.iterrows():
            st.write(f"🕒 {row['waktu']} - ✍️ {row['nama']}: {row['komentar']}")