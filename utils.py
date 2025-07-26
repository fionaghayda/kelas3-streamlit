import streamlit as st

# Mapping password sesuai halaman
PASSWORDS = {
    "nilai": "kelas3ku",
    "data": "kelas3ku",
    "komentar": "ortu3ku",
    "galeri": "ortu3ku"
}

def check_password(page: str) -> bool:
    """Menampilkan form password untuk halaman tertentu."""
    st.warning("🔒 Halaman ini dilindungi. Masukkan password untuk mengakses.")
    with st.form(f"Login_{page}"):
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")
        if submitted:
            if password == PASSWORDS.get(page):
                st.success("✅ Akses diterima.")
                st.session_state[f"auth_{page}"] = True
            else:
                st.error("❌ Password salah.")
                st.session_state[f"auth_{page}"] = False

    return st.session_state.get(f"auth_{page}", False)
