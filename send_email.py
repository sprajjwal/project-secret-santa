import smtplib 
import os
  
def send_email(draws, info_dict):
    """sends email to everyone with their draw by getting their
    email from email_dict"""
    # creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    
    # start TLS for security 
    s.starttls() 
    sender = "findmysecretsanta@gmail.com"

    # Authentication 
    s.login(sender, os.environ['PASSWORD']) 
    
    for sender in draws.keys():

        # message to be sent 
        message = f"""\
Subject: Your secret santa draw.


Hi {sender},
You are {draws[sender]}'s secret santa. {draws[sender]}'s email is {info_dict[draws[sender]][0]}.
{draws[sender]}'s address is: {info_dict[draws[sender]][1]}
"""
        
        # sending the mail 
        s.sendmail(sender, info_dict[sender][0], message) 
    
    # terminating the session 
    s.quit() 

if __name__ == "__main__":
    draws = {
        'shaash': 'shashwat',
    }
   
    info_dict = {
        'shaash': ["findmysecretsanta@gmail.com", "851 california street, San francisco, 94108"],
        'shashwat': ["meshashwat007@gmail.com", "851 california street, San francisco, 94108"]
    }

    send_email(draws, info_dict)