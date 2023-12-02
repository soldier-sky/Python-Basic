import smtplib
from email.message import EmailMessage

# Note: This example may not work with Azur or google out of the box. Below example is contain basic skeleton only.
# Use app password to send email via python.

email = EmailMessage()
email['from'] = 'Sunil Yadav'
email['to'] = 'sunil.dummy@mydomain.com'
email['subject'] = 'Test email from python'

email.set_content('This emal is test message to validate the email using python')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()  # send hello to smtp that sent I'm alive kind of signal
    smtp.starttls()  # enables tls. Read more on how to configure certificate etc
    smtp.login('myemailaddress@gmail.com', 'mypassword')
    smtp.send_message(email)
    print('Sent successfully!')