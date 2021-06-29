# Python code to illustrate Sending mail from
# your Gmail account
import smtplib
def user(ema,message):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("darpantrivedi507289@gmail.com", "kano@9824")
    s.sendmail("darpantrivedi507289@gmail.com", ema, message)
    s.quit()
