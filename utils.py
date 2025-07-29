import streamlit as st
import pandas as pd

def login_user():
    users_df = pd.read_csv("data/users.csv")
    
    with st.sidebar:
        st.subheader("🔐 Login Pengguna")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        login_btn = st.button("Login")

    if login_btn:
        user = users_df[(users_df['username'] == username) & (users_df['password'] == password)]
        if not user.empty:
            st.session_state['login'] = True
            st.session_state['username'] = user.iloc[0]['username']
            st.session_state['role'] = user.iloc[0]['role']
            st.success(f"Berhasil login sebagai {user.iloc[0]['role']}")
        else:
            st.error("Username atau password salah!")

def is_logged_in():
    return st.session_state.get("login", False)

def get_user_role():
    return st.session_state.get("role", None)
