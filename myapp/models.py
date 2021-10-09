from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=32, unique=True, null=False, blank=False)
    pwd = models.CharField(max_length=32, null=False)
    phone = models.CharField(max_length=32)
    address = models.CharField(max_length=256)
    create_time = models.DateTimeField(auto_now_add=True)
    avatar = models.ImageField(upload_to='avatar', default='media/avatar.png')

    class Meta:
        db_table = 'user'


class PowerPosition(models.Model):
    position = models.CharField(max_length=64)
    parent = models.ForeignKey('self',related_name='children',on_delete=models.SET_NULL,null=True,blank=True)

    class Meta:
        db_table = "power"

