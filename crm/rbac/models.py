from django.db import models

# Create your models here.

class Permission(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32, verbose_name="标题", default="", unique=True)
    permission = models.CharField(max_length=32, verbose_name="权限", unique=True)
    



class Role(models.Model):
    id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=32, verbose_name="角色名", unique=True)
    permission_id = models.ManyToManyField(Permission, verbose_name="所拥有的的权限", null=True, blank=True)




class UserInfo(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=32, verbose_name="用户名", unique=True)
    role_id = models.ManyToManyField(Role, verbose_name="所拥有的的角色", null=True, blank=True)

