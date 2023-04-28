from django.db import models

# Create your models here.


class Permission(models.Model):
    title = models.CharField(verbose_name='标题', max_length=32)
    url = models.CharField(verbose_name='含正则的URL', max_length=128)
    is_menu = models.BooleanField(verbose_name="是否可以做菜单", default=False)
    icon = models.CharField(verbose_name="图标", max_length=32, null=True, blank=True)

    def __str__(self):
        return self.title

class Role(models.Model):
    title = models.CharField(verbose_name='角色名称', max_length=32)
    permission = models.ManyToManyField(verbose_name='所拥有的权限', to='Permission', blank=True)

    def __str__(self):
        return self.title

class UserInfo(models.Model):
    name = models.CharField(verbose_name='用户名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=64)
    roles = models.ManyToManyField(verbose_name='所拥有的角色', to='Role', blank=True)

    def __str__(self):
        return self.name