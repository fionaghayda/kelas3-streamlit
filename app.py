import streamlit as st
import pandas as pd

# Konfigurasi halaman
st.set_page_config(page_title="Dokumentasi Kelas 3", layout="wide")

# CSS untuk dekorasi dan tata letak
st.markdown("""
    <style>
        .big-title {
            font-size: 40px;
            font-weight: 800;
            margin-bottom: -10px;
        }
        .sub-title {
            font-size: 22px;
            font-weight: 600;
            color: #333333;
            margin-bottom: 10px;
        }
        .author {
            font-size: 16px;
            color: gray;
            margin-bottom: 10px;
        }
        .top-line {
            border-top: 4px solid #f39c12;
            margin-top: -30px;
            margin-bottom: 15px;
        }
        .divider {
            border-top: 1px solid #ddd;
            margin-top: 25px;
            margin-bottom: 15px;
        }
        .section-title {
            font-size: 28px;
            font-weight: bold;
            margin-bottom: 5px;
            color: #2c3e50;
        }
        .emoji {
            font-size: 32px;
            margin-right: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Header Utama
st.markdown('<div class="top-line"></div>', unsafe_allow_html=True)
st.markdown('<div class="big-title">📘 Dokumentasi Akademik Kelas 3</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">SDN Wonoplintahan 1 - Kecamatan Prambon, Sidoarjo</div>', unsafe_allow_html=True)
st.markdown('<div class="author">👩‍🏫 Oleh: Ibu RINI KUS ENDANG, S.Pd</div>', unsafe_allow_html=True)

# Garis pemisah
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Seksi Selamat Datang
st.markdown('<div class="section-title">👋 Selamat Datang!</div>', unsafe_allow_html=True)
st.write("Website ini dibuat untuk mendokumentasikan kegiatan pembelajaran dan informasi penting yang bisa diakses oleh orang tua murid dan wali kelas.")

# Garis pemisah
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Jadwal Pelajaran
st.markdown('<div class="section-title">📅 Jadwal Pelajaran Mingguan</div>', unsafe_allow_html=True)

try:
    jadwal = pd.read_csv("https://raw.githubusercontent.com/cklothoz79/kelas3-streamlit/main/data/jadwal_pelajaran.csv")
    for hari in jadwal['Hari'].unique():
        st.subheader(f"📖 {hari}")
        df_hari = jadwal[jadwal['Hari'] == hari].drop(columns=["Hari"])
        st.dataframe(df_hari, hide_index=True, use_container_width=True)
except Exception as e:
    st.error("Tidak dapat memuat data jadwal. Pastikan file `jadwal_pelajaran.csv` ada di folder `/data`.")

# Garis pemisah akhir
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
