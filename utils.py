import streamlit as st

def check_teacher_password():
    correct_password = "kelas3ku"
    if "teacher_auth" not in st.session_state:
        st.session_state.teacher_auth = False

    if not st.session_state.teacher_auth:
        password = st.text_input("🔐 Masukkan Password Bu Rini", type="password")
        if password == correct_password:
            st.session_state.teacher_auth = True
            st.success("✅ Akses Diberikan")
        elif password != "":
            st.error("❌ Password salah")
            return False
        else:
            return False
    return True

def check_guest_password():
    correct_password = "orangtuaku"
    if "guest_auth" not in st.session_state:
        st.session_state.guest_auth = False

    if not st.session_state.guest_auth:
        password = st.text_input("🔐 Masukkan Password Orang Tua/Guru", type="password")
        if password == correct_password:
            st.session_state.guest_auth = True
            st.success("✅ Akses Diberikan")
        elif password != "":
            st.error("❌ Password salah")
            return False
        else:
            return False
    return True
