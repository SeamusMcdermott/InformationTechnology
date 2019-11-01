import smtplib

email = 'goodshepherdiot@gmail.com'  # your
password = 'P@ssword#1'  # your email account password
send_to_email = 'seamuscmcd@hotmail.com'  # recipient
message = 'Yes this in the message'  # message in body of email


server = smtplib.SMTP('smtp.gmail.com', 587)  # connect to the server
server.starttls()
server.login (email, send_to_email, message)
server.sendmail(email, send_to_email, message)


server.quit()