import smtplib 
import os
  
def send_email(draws, email_dict, address_dict):
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
You are {draws[sender]}'s secret santa. {draws[sender]}'s email is {email_dict[draws[sender]]}.
{draws[sender]}'s address is: {address_dict[draws[sender]]}
"""
        
        # sending the mail 
        s.sendmail(sender, email_dict[draws[sender]], message) 
    
    # terminating the session 
    s.quit() 

if __name__ == "__main__":
    draws = {
        'shaash': 'shashwat',
    }
    email_list = {
        'shaash': "findmysecretsanta@gmail.com",
        'shashwat': "meshashwat007@gmail.com"
    }
    address_dict = {
        'shaash': "851 california street, San francisco, 94108",
        'shashwat': "851 california street, San francisco, 94108"
    }

    send_email(draws, email_list, address_dict)