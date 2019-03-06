from django.db import models

# Create your models here.

class Game(models.Model):
    status=models.BooleanField(default=False)
    create_time=models.DateTimeField(auto_now_add=True)
    game_name=models.CharField(max_length=32, unique=True)
    duty_user=models.CharField(max_length=32)
    game_region=models.CharField(max_length=16)
    game_alert=models.BooleanField(default=False)
    alert_count=models.IntegerField()
    last_alert_time=models.DateTimeField(auto_now_add=True)

class Region(models.Model):
    region_name=models.CharField(max_length=32)
    whether_alert=models.ForeignKey(Game,on_delete=models.CASCADE,default=False)
    create_time=models.DateTimeField(auto_now_add=True)

class Alert(models.Model):
    status=models.BooleanField(default=False)
    phone=models.CharField(max_length=16)
    mail=models.EmailField(max_length=20)
    wechat=models.CharField(max_length=32)
    create_time=models.DateTimeField(auto_now_add=True)
    timeslot_start=models.DateTimeField(default=None)
    timeslot_stop=models.DateTimeField(default=None)
    threshold_value=models.FloatField(max_length=16)

class UserList(models.Model):
    username=models.CharField(max_length=16)
    phone=models.CharField(max_length=16)
    mail=models.EmailField(max_length=20)
    program=models.CharField(max_length=16)
    whether_alert=models.BooleanField(default=False)
    create_time=models.DateTimeField(auto_now_add=True)






