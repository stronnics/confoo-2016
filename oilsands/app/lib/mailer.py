import sys, io
import sendgrid
from config import SENDGRID_LOGIN, SENDGRID_PASSWORD

class SendGrid(object):

  def __init__(self):
  
    self.login = SENDGRID_LOGIN
    self.password = SENDGRID_PASSWORD

  def send(self, origin, destination, subject, content, attachment_name=None, attachment_path=None):
    sg = sendgrid.SendGridClient(self.login, self.password)

    mail = sendgrid.Mail()

    for dest in destination:
      mail.add_to(dest)

    mail.set_from(origin)
    mail.set_subject(subject)
    mail.set_html(content)

    if attachment_path and attachment_name:
      mail.add_attachment(attachment_name, attachment_path)

    status, msg = sg.send(mail)
    return {'status': status, 'message': msg}
