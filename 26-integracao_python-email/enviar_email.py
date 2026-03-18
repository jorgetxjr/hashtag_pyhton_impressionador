#SMTP

import smtplib
import email.message

def enviar_email():
    msg = email.message.Message()
    msg["Subject"] = "Email enviado com o python"
    msg["From"] = "jorgetxjr@gmail.com"
    msg["To"] = "jorgetxjr@gmail.com"
    #msg["Cc"] ="cópia de mensagem"
    #msg["Bcc"] = "cópia oculta de mensagem"

    corpo_email="<p>boa tarde</p>" \
    "<p>teste de email com o python e smtplib</p>"

    corpo_email=corpo_email.encode("utf-8")
    
    msg.add_header("Content-type", "text/html")
    msg.set_payload(corpo_email)

    servidor = smtplib.SMTP("smtp.gmail.com", 587)
    servidor.starttls()
    servidor.login("username", "password")
    servidor.send_message(msg)
    servidor.quit()

enviar_email()