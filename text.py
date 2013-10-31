#!/usr/bin/env python
import sys
import smtplib

def send(body, to = "INSERT PHONE NUMBER", username = "INSERT GMAIL ADDRESS", password = "INSERT PASSWORD"):
  mail_server = smtplib.SMTP("smtp.gmail.com", 587)
  mail_server.ehlo()
  mail_server.starttls()
  mail_server.login(username, password)
  mail_server.sendmail(username, to, body)
  mail_server.close()

if __name__ == '__main__':
  argc = len(sys.argv)

  # first argument is the text message
  if argc == 2:
    send(sys.argv[1])
  # arguments are a text message and an email
  elif argc == 3:
    send(sys.argv[1], sys.argv[2])
  else:
    print 'Usage: gmail.py "Text message" "[phone number as email]"'
