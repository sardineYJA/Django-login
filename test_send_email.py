import os
from django.core.mail import send_mail

# 测试发送邮箱功能

# 单独运行此py文件，无法自动链接Django环境，需要通过os模块对环境变量进行设置
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
if __name__ == '__main__':
    send_mail(
        '来着Django测试邮箱',              # 主题
        '这是内容',                        # 内容
        '157XXXXX@sina.cn',             # 发送方，需要和settings中的一致
        ['XXXXX@qq.com'],          # 接收方列表
    )
    print('OK')

