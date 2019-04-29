from django.db import models

# Create your models here.


class User(models.Model):
    gender = (('male', "男"), ('female', "女"),)
    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default="男")
    c_time = models.DateTimeField(auto_now_add=True)
    has_confirmed = models.BooleanField(default=False)   # 邮箱是否确认

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-c_time']    # 按创建时间反序排列
        verbose_name = '用户'
        verbose_name_plural = "用户"


# 保存用户和注册码之间的关系，一对一形式
class ConfirmString(models.Model):
    code = models.CharField(max_length=256)                            # code是哈希后的注册码
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    c_time = models.DateTimeField(auto_now_add=True)                   # 注册的提交时间

    def __str__(self):
        return self.user.name + ": " + self.code

    class Meta:
        ordering = ['-c_time']
        verbose_name = '确认码'
        verbose_name_plural = '确认码'


