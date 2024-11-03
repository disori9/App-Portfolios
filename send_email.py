import smtplib
import ssl

def send_email(user_email, user_message):
    host = "smtp.gmail.com"
    port = 465

    username = "violetori99@gmail.com"
    receiver = username
    password = "nsujziuofmbpieno"

    context = ssl.create_default_context()

    message_local = f"""\
Subject: Porfolio Email

From: {user_email}
{user_message}
"""

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message_local)