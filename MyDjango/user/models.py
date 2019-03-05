from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
class MyUser(AbstractUser):
    qq = models.CharField('QQ号码',max_length = 16)
    weChat = models.CharField('微信账号', max_length = 100)
    mobile = models.CharField('手机号码', max_length = 11)
    def __str__(self):
        return self.username