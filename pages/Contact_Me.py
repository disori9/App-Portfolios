import streamlit as st
import send_email

st.header("Contact Me")

with st.form(key='user_emails'):
    user_email = st.text_input("Enter your email address")
    user_message = st.text_area("Enter your message")
    submit_msg = st.form_submit_button(label='Send')

    if submit_msg:
        send_email.send_email(user_email, user_message)