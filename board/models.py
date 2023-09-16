from django.db import models

class user_master(models.Model):
    id_seq = models.AutoField(primary_key='TRUE')
    user_id = models.CharField(max_length=32,null="FALSE")
    user_pw = models.CharField(max_length=20,null="FALSE")
    user_name = models.CharField(max_length=20, default='이름을 설정하세요')
    user_email = models.CharField(max_length=32, default='E-mail을 설정하세요')
    user_activate = models.CharField(max_length=8, default='0')

class email_setting(models.Model):
    mail_seq = models.AutoField(primary_key='True')
    mail_sender_host = models.CharField(max_length=30,null="FALSE")
    smtp_port = models.CharField(max_length=12,null="FALSE")
    sender_user = models.CharField(max_length=24,null="FALSE")
    sender_password = models.CharField(max_length=30,null="FALSE")

class email_log(models.Model):
    mail_seq=models.AutoField(primary_key='True')
    mail_title=models.CharField(max_length=200,null="FALSE")
    mail_to=models.CharField(max_length=200,null="FALSE")
    mail_from=models.CharField(max_length=200,null="FALSE")
    mail_body=models.CharField(max_length=200,null="FALSE")
    mail_bcc=models.CharField(max_length=200,null="FALSE")
    mail_datetime= models.DateTimeField(auto_now_add=True)

# Create your models here.
