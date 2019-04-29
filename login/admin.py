from django.contrib import admin

# Register your models here.

from . import models
admin.site.register(models.User)          # 在admin注册模型
admin.site.register(models.ConfirmString)

