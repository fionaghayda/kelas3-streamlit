import streamlit as st
import pandas as pd
import os

DATA_FILE = "data/galeri.csv"


def load_data():
    if os.path.exists(DATA_FILE):
        return pd.read_csv(DATA_FILE)
    return pd.DataFrame(columns=["Tanggal", "Deskripsi", "Gambar"])


def save_data(df):
    df.to_csv(DATA_FILE, index=False)


def show_galeri_page():
    st.header("📷 Galeri Kegiatan")
    df = load_data()

    # Tambah Galeri Baru
    st.subheader("Tambah Foto Galeri Baru")
    with st.form("Tambah Galeri"):
        tanggal = st.date_input("Tanggal")
        deskripsi = st.text_input("Deskripsi")
        gambar = st.text_input("Nama File Gambar (di folder images)")
        submitted = st.form_submit_button("Tambah")
        if submitted:
            new_data = pd.DataFrame([[tanggal, deskripsi, gambar]], columns=["Tanggal", "Deskripsi", "Gambar"])
            df = pd.concat([df, new_data], ignore_index=True)
            save_data(df)
            st.success("Foto galeri berhasil ditambahkan!")

    st.markdown("---")

    # Tampilkan dan Edit Galeri
    st.subheader("🖼️ Daftar Galeri")
    for i, row in df.iterrows():
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"**{row['Tanggal']}** - {row['Deskripsi']}")
            if row['Gambar']:
                st.image(f"images/{row['Gambar']}", width=300)
        with col2:
            if st.button("✏️ Edit", key=f"edit_{i}"):
                with st.form(f"edit_form_{i}"):
                    new_tanggal = st.date_input("Tanggal", value=pd.to_datetime(row['Tanggal']))
                    new_deskripsi = st.text_input("Deskripsi", value=row['Deskripsi'])
                    new_gambar = st.text_input("Nama File Gambar", value=row['Gambar'])
                    update = st.form_submit_button("Update")
                    if update:
                        df.at[i, 'Tanggal'] = new_tanggal
                        df.at[i, 'Deskripsi'] = new_deskripsi
                        df.at[i, 'Gambar'] = new_gambar
                        save_data(df)
                        st.success("Galeri berhasil diperbarui.")
                        st.experimental_rerun()
            if st.button("🗑️ Hapus", key=f"hapus_{i}"):
                df = df.drop(i).reset_index(drop=True)
                save_data(df)
                st.success("Galeri berhasil dihapus.")
                st.experimental_rerun()
