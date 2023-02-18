from django.db import models

# Create your models here.
# 사용자가 원하는 온,습도 설정 


class UserData(models.Model):
    Userid = models.CharField(max_length=200, primary_key=True)
    UserTemp = models.IntegerField(default=19) # 18~26 
    UserHumid = models.IntegerField(default=55) # 0~100% 보통 40~70
    Philipshuetoken = models.CharField(max_length=200, default=0)
    Smartthingstoken = models.CharField(max_length=200, default=0)
    Userlocation = models.CharField(max_length=10,default='종로구')     
    def __str__(self):
        return self.Userid



