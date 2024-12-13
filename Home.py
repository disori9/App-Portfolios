import streamlit as st
import pandas

#st.set_page_config(layout='wide')

col1, col2 = st.columns(2)
with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Ori")
    description = """Good morning. I am Ori, a student, and these are my Python projects.
    Feel free to explore! My dream is to become a data engineer, and I hope this would
    be a good progress for that. Here's to life and for the future!"""
    st.info(description)

st.write("Below you can find some of the apps I have built in Python. Feel free to contact me!")

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])
data_frame = pandas.read_csv('data.csv', sep=";", on_bad_lines='skip')

with col3:
    for index, row in data_frame[:8].iterrows():
        st.header(row['title'])
        st.image(f'images/{row["image"]}', width=300)
        st.write(row['description'])
        st.write(f'[Source Code]({row["url"]})')

with col4:
    for index, row in data_frame[8:].iterrows():
        st.header(row['title'])
        st.image(f'images/{row["image"]}', width=300)
        st.write(row['description'])
        st.write(f'[Source Code]({row["url"]})')