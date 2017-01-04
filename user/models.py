import django
from django.contrib.auth.hashers import make_password
from django.db import models


# Create your models here.


class User(models.Model):
    tel = models.CharField(u'电话', max_length=11, db_index=True, unique=True)
    password = models.CharField(u'密码', max_length=128)
    email = models.EmailField(blank=True)
    data_joined = models.DateTimeField(u'创建时间', auto_now_add=True)
    birthday = models.DateField(blank=True, auto_now_add=True)

    @staticmethod
    def createUser(tel, password):
        final_password = make_password(password, None, 'pbkdf2_sha256')
        user = User(tel=tel, password=final_password)
        user.save()
