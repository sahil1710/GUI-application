import tkinter as tk
from tkinter import ttk
from tkinter import *
import smtplib


def email(root):
    ttk.Label(root, text="From-Email : ", font = ("poppins", 10)).grid(row=0, column=10, padx=60, pady=5)
    from_email = ttk.Entry(root, width=70)
    from_email.grid(row=0, column=11)

    ttk.Label(root, text="Password : ", font = ("poppins", 10)).grid(row=1, column=10, padx=60, pady=5)
    from_email_password = ttk.Entry(root, width=70)
    from_email_password.grid(row=1, column=11)

    ttk.Label(root, text="To-Email : ", font = ("poppins", 10)).grid(row=2, column=10, padx=60, pady=5)
    to_email = ttk.Entry(root, width=70)
    to_email.grid(row=2, column=11)

    ttk.Label(root, text="Subject : ", font = ("poppins", 10)).grid(row=3, column=10, padx=60, pady=5)
    subject = ttk.Entry(root, width=70)
    subject.grid(row=3, column=11)

    ttk.Label(root, text="Message ", font = ("poppins", 10)).grid(row=4, column=10, padx=60, pady=5)
    mail_body = Text(root, height = 5, width = 52)
    mail_body.grid(row=4, column=11)


    def send_mail():
        f_mail = from_email.get()
        f_mail_password = from_email_password.get()
        t_mail = to_email.get()
        sub = subject.get()
        text = mail_body.get(1.0, "end-1c")

        message = 'Subject: {}\n\n{}'.format(sub, text)

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(f_mail, f_mail_password)
        server.sendmail(f_mail, t_mail, message)
        server.quit()

        print("Mail Sent Successfully!")

        # After Sending Mail Delete all data of input fields
        from_email.delete(0, END)
        from_email_password.delete(0, END)
        to_email.delete(0, END)
        subject.delete(0, END)
        mail_body.delete("1.0", "end")


    send_button = ttk.Button(root, text="Send", command=send_mail, width=30)
    send_button.grid(row=5, column=11, pady=20)
