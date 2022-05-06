import smtplib
from email.message import EmailMessage
import imghdr
import re
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

def sendEmail(addr):
    reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
    if bool (re.match(reg, addr)):
        smtp.send_message(message)
        print("정상적으로 메일이 발송되었습니다.")
    else:
        print("유효한 이메일 주소가 아닙니다.")

message = EmailMessage()
message.set_content("저는 황서경입니다.")

message["Subject"] = "메일 보내볼게요."
message["From"] = "2012187@sookmyung.ac.kr"
message["To"] = "purewater7174@gmail.com"

with open("codelion.jpeg", "rb") as image:
    image_file = image.read()

image_type = imghdr.what('codelion', image_file)
message.add_attachment(image_file, maintype='image', subtype=image_type)

smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
smtp.login("purewater7174@gmail.com", "hsk756371!")

sendEmail("purewater7174@gmail.com")
smtp.quit()