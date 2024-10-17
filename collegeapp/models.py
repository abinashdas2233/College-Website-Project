import uuid
from django.db import models

# Create your models here.
class userregistration(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    contact_no=models.CharField(max_length=15)
    email_id=models.CharField(max_length=100)
    role=models.CharField(max_length=10)
    password=models.CharField(max_length=15)
class dues(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    branch=models.CharField(max_length=30)
    Fee=models.BigIntegerField()
    due_amount=models.BigIntegerField()
    cleared_dues=models.BigIntegerField()
class notification(models.Model):
    notice_no=models.IntegerField(primary_key=True)
    date_time=models.DateTimeField(auto_now_add=True)
    notice=models.CharField(max_length=1000)
class feedback(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    contactno=models.IntegerField()
    email_id=models.CharField(max_length=20)
    role=models.CharField(max_length=10)
    message=models.CharField(max_length=1000)

class course(models.Model):
    id=models.AutoField(primary_key=True)
    subject=models.CharField(max_length=1000)
    Branch=models.CharField(max_length=100)
    link=models.CharField(max_length=1000)
