import streamlit as st

# Fungsi autentikasi berdasarkan halaman

def check_password_kelas():
    def password_entered():
        if st.session_state["password_kelas"] == st.secrets["password_kelas"]:
            st.session_state["password_correct_kelas"] = True
            del st.session_state["password_kelas"]
        else:
            st.session_state["password_correct_kelas"] = False

    if "password_correct_kelas" not in st.session_state:
        st.text_input(
            "Masukkan password untuk akses Data Siswa dan Nilai:",
            type="password",
            on_change=password_entered,
            key="password_kelas",
        )
        return False
    elif not st.session_state["password_correct_kelas"]:
        st.text_input(
            "Masukkan password untuk akses Data Siswa dan Nilai:",
            type="password",
            on_change=password_entered,
            key="password_kelas",
        )
        st.error("Password salah.")
        return False
    else:
        return True

def check_password_galeri():
    def password_entered():
        if st.session_state["password_galeri"] == st.secrets["password_galeri"]:
            st.session_state["password_correct_galeri"] = True
            del st.session_state["password_galeri"]
        else:
            st.session_state["password_correct_galeri"] = False

    if "password_correct_galeri" not in st.session_state:
        st.text_input(
            "Masukkan password untuk akses Galeri dan Komentar:",
            type="password",
            on_change=password_entered,
            key="password_galeri",
        )
        return False
    elif not st.session_state["password_correct_galeri"]:
        st.text_input(
            "Masukkan password untuk akses Galeri dan Komentar:",
            type="password",
            on_change=password_entered,
            key="password_galeri",
        )
        st.error("Password salah.")
        return False
    else:
        return True
