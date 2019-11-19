import smtplib 
  
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
sender = "findmysecretsanta@gmail.com"

# Authentication 
s.login(sender, "prajjwal12345") 
  
# message to be sent 
message = "Message_you_need_to_send"
  
# sending the mail 
s.sendmail(sender, "meshashwat007@gmail.com", message) 
  
# terminating the session 
s.quit() 