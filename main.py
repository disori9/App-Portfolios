import streamlit as st

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Ori")
    description = """Good morning. I am Ori, a student, and these are my Python projects.
    Feel free to explore! My dream is to become a data engineer, and I hope this would
    be a good progress for that. Here's to life and for the future!"""
    st.info(description)