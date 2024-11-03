import smtplib
import ssl

host = "smtp.gmail.com"
port = 465

username = "violetori99@gmail.com"
password = "nsujziuofmbpieno"

receiver = username
context = ssl.create_default_context()
message = """\
Subject: Hello!
HI!!!
"""
with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)