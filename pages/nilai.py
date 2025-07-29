import streamlit as st
import pandas as pd
import os

def show_nilai_page():
    st.header("📊 Rekap Nilai dan Data Siswa")
    try:
        df_nilai = pd.read_csv("data/nilai.csv")
        st.subheader("Rekap Nilai")
        st.dataframe(df_nilai, use_container_width=True)
    except FileNotFoundError:
        st.warning("File nilai.csv tidak ditemukan.")

    try:
        df_siswa = pd.read_csv("data/siswa.csv")
        st.subheader("Data Siswa")
        st.dataframe(df_siswa, use_container_width=True)
    except FileNotFoundError:
        st.warning("File siswa.csv tidak ditemukan.")