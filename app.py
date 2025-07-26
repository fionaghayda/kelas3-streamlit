# Beranda (Dashboard + Jadwal)
if menu == "Beranda":
    st.header("Selamat datang di dokumentasi akademik kelas 3!")
    st.write("""
        Website ini dibuat untuk mendokumentasikan kegiatan pembelajaran dan informasi penting 
        yang bisa diakses oleh orang tua murid dan wali kelas.
    """)

    st.subheader("📆 Jadwal Pelajaran Mingguan")
    try:
        df_jadwal = pd.read_csv("data/jadwal_pelajaran.csv")

        # Ganti nilai kolom "Hari" yang duplikat menjadi kosong
        df_jadwal["Hari"] = df_jadwal["Hari"].mask(df_jadwal["Hari"].duplicated(), "")

        # Tampilkan jadwal dalam bentuk tabel
        st.table(df_jadwal)
    except FileNotFoundError:
        st.error("File jadwal_pelajaran.csv belum ditemukan di folder 'data/'.")
