import streamlit as st
import os
import pandas as pd

def show_galeri_page(role):
    st.header("🖼️ Galeri Foto")
    folder = "data/galeri"
    os.makedirs(folder, exist_ok=True)
    caption_file = "data/captions.csv"

    if role == "guru":
        uploaded = st.file_uploader("Unggah foto", type=["jpg","jpeg","png"])
        caption = st.text_input("Caption foto")
        if st.button("Simpan Foto") and uploaded:
            path = os.path.join(folder, uploaded.name)
            with open(path, "wb") as f:
                f.write(uploaded.getbuffer())
            with open(caption_file, "a") as f:
                f.write(f"{uploaded.name},{caption}\n")
            st.success("✅ Foto berhasil diunggah!")

    captions = {}
    if os.path.exists(caption_file):
        with open(caption_file, "r") as f:
            for line in f:
                name, text = line.strip().split(",",1)
                captions[name]=text

    files = os.listdir(folder)
    for file in files:
        if file.endswith((".jpg",".jpeg",".png")):
            st.image(os.path.join(folder,file),width=400)
            st.caption(captions.get(file,""))
            if role == "guru":
                if st.button(f"Hapus {file}"):
                    os.remove(os.path.join(folder,file))
                    captions.pop(file,"")
                    pd.DataFrame(list(captions.items()),columns=["file","caption"]).to_csv(caption_file,index=False)
                    st.experimental_rerun()