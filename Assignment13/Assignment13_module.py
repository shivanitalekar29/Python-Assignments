from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from sys import *
import os
import datetime
import hashlib
import time

def hashfile(path, blocksize = 1024):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()

def ddlog_file(file,log_dir = 'Nice'):
    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    if os.path.exists(log_dir):
        file_name = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")+".txt"
        file_path = os.path.join(log_dir, file_name) 
        filn = open(file_path, 'a')
        for i in file:
            filn.write(i)
            filn.write('\n')
        return file_path

def email_sending(re_email,tfn,dfn,file_name,time1):
    toadd = re_email
    fromadd = "shivanitalekar29.st@gmail.com"
    body = f"1. Starting time of scanning : {str(time1)} \n2. Total number of files scanned :{str(tfn)} \n3. Total number of duplicate files :{str(dfn)}"
    subject = "Duplicate file record"

    msg = MIMEMultipart()
    msg['to'] = toadd
    msg['from'] = fromadd
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
            server.sendmail(fromadd, toadd, text)
            server.quit()
            print("Email sent successfully with attachment.")
        except Exception as e:
            print(f"Unable to send email: {str(e)}")
        
def duplicate(path1,email_1):
    path = path1

    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)    
    exists = os.path.isdir(path)

    if exists:
        duplicate_file = []
        filedups = 0
        count_TNF = 0
        count_DNF = 0
        time1 = 0
        for dirName, subdirs, fileList in os.walk(path):
            for filen in fileList:
                path = os.path.join(dirName, filen)
                file_hash = hashfile(path)
                count_TNF = count_TNF + 1
                if file_hash == filedups:
                    t = time.localtime()
                    time1 = time.strftime("%H:%M:%S", t)
                    count_DNF = count_DNF + 1
                    duplicate_file.append(filen)
                    os.remove(path)
                filedups = file_hash
        duplicateFile = ddlog_file(duplicate_file)
        email_sending(email_1,count_TNF,count_DNF,duplicateFile,time1)
    else:
        print("Invalid Path")
