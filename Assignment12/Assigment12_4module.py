from email.mime.multipart import MIMEMultipart
import psutil
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText

def ProcessDisplay():
    listprocess = []
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
            listprocess.append(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return listprocess

def fileoutput(directory_name):
    listprocess = ProcessDisplay()
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
    file_name = "Log221.txt"
    file_path = os.path.join(directory_name, file_name)
    with open(file_path, 'w') as output_file:
        for elem in listprocess:
                output_file.write(str(elem))
    return file_path


def email1(file_path,remail_id):
    file_name = file_path
    sender_email = 'shivanitalekar29.st@gmail.com'
    recipient_email = remail_id
    subject = "Email with Attachment"
    body = "Please see the attached file."

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body,'plain'))
    with open(file_name, 'rb') as file:
        attachment = MIMEApplication(file.read(), _subtype="txt")
        attachment.add_header('Content-Disposition', 'attachment', filename=file_name)
        msg.attach(attachment)


    smtp_server = "smtp.gmail.com"  
    smtp_port = 587 
    smtp_username = 'shivanitalekar29.st@gmail.com' 
    smtp_password = 'kfdo qdeh kluv qaks'

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()
        print("Email sent successfully with attachment.")
    except Exception as e:
     print(f"Unable to send email: {str(e)}")