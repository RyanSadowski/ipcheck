# ipcheck.py

import time
import requests
import smtplib

gmail_address = 'xxxx@gmail.com'                                    # This is our new gmail address that we created.
gmail_password = '********'                                         # This is the password to that email address.
to_email = 'to@email.com'                                           # This is where we want to recieve the email
sleep_for = 600 # 600 = 10 min                                      # Time between IP Checks
ip = ''                                                             # Initialize our ip variable

def SendEmail(ip):                                                  # SendEmail function takes in the ip variable
    try:
      server = smtplib.SMTP('smtp.gmail.com',587)
      server.ehlo()
      server.starttls()
      server.ehlo()
      server.login(gmail_address, gmail_password)
      server.sendmail(gmail_address, to_email ,ip)
      server.close()
    except:
        print "Error: unable to send email"

while True:
    if(requests.get('http://api.ipify.org/').status_code == 200):
        r = requests.get('http://api.ipify.org')
        if (ip == r.text):
            print 'no change in IP'
        else:
            ip = r.text
            print ip + ' is the new IP'
            SendEmail(ip)                                             # Call the SendEmail Function and pass in our ip variable
    else:
        print 'error getting ip'
    time.sleep(sleep_for)
