import streamlit as st
import pandas as pd

def get_session():
    return st.session_state

def login_user():
    st.subheader("🔑 Login Pengguna")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        try:
            users = pd.read_csv("users.csv")
            user = users[(users["username"] == username) & (users["password"] == password)]
            if not user.empty:
                st.session_state["logged_in"] = True
                st.session_state["username"] = user.iloc[0]["username"]
                st.session_state["role"] = user.iloc[0]["role"]
                st.experimental_rerun()
            else:
                st.error("❌ Username atau password salah")
        except FileNotFoundError:
            st.error("File users.csv tidak ditemukan")

def logout_user():
    st.session_state.clear()
