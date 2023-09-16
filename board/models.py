from django.db import models

class user_master(models.Model):
    id_seq = models.AutoField(primary_key='TRUE')
    user_id = models.CharField(max_length=32,null="FALSE")
    user_pw = models.CharField(max_length=20,null="FALSE")
    user_name = models.CharField(max_length=20, default='이름을 설정하세요')
    user_email = models.CharField(max_length=32, default='E-mail을 설정하세요')

class email_setting(models.Model):
    mail_seq = models.AutoField(primary_key='True')
    mail_sender_host = models.CharField(max_length=30,null="FALSE")
    smtp_port = models.CharField(max_length=12,null="FALSE")
    sender_user = models.CharField(max_length=24,null="FALSE")
    sender_password = models.CharField(max_length=30,null="FALSE")

# Create your models here.
