import streamlit as st

PASSWORD_RINI = "kelas3ku"
PASSWORD_TAMU = "galeriku"

def check_password():
    def password_entered():
        if st.session_state["password_rini"] == PASSWORD_RINI:
            st.session_state["rini_auth"] = True
        else:
            st.session_state["rini_auth"] = False
            st.error("Password salah.")

    if "rini_auth" not in st.session_state:
        st.text_input("Masukkan Password Halaman", type="password", key="password_rini", on_change=password_entered)
        return False
    elif not st.session_state["rini_auth"]:
        st.text_input("Masukkan Password Halaman", type="password", key="password_rini", on_change=password_entered)
        return False
    else:
        return True

def check_guest_password():
    def password_entered():
        if st.session_state["password_tamu"] == PASSWORD_TAMU:
            st.session_state["tamu_auth"] = True
        else:
            st.session_state["tamu_auth"] = False
            st.error("Password salah.")

    if "tamu_auth" not in st.session_state:
        st.text_input("Masukkan Password Galeri/Komentar", type="password", key="password_tamu", on_change=password_entered)
        return False
    elif not st.session_state["tamu_auth"]:
        st.text_input("Masukkan Password Galeri/Komentar", type="password", key="password_tamu", on_change=password_entered)
        return False
    else:
        return True
