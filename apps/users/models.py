from datetime import datetime

from django.db import models
# 继承后台auth_user字段,并增加自己定义的字段
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50,verbose_name='昵称',default='')
    birthday = models.DateField(verbose_name='生日',null=True,blank=True)
    gender = models.CharField(max_length=10,choices=(('male','男'),('female','女')),default='female')
    address = models.CharField(max_length=100,default='')
    mobile = models.CharField(max_length=11,null=True)
    image = models.ImageField(upload_to='image/%Y/%m',default='image/default.png',max_length=100)

    #表明
    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    # 获取用户未读消息的数量
    def unread_nums(self):
        from operation.models import UserMessage
        return UserMessage.objects.filter(user=self.id, has_read=False).count()

    def __str__(self):
        return self.username

# 邮箱验证
class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20,verbose_name='验证码')
    email = models.EmailField(max_length=50,verbose_name='邮箱')
    send_type = models.CharField(choices=(('register','注册'),('forget','找回密码'),('update_email','修改邮箱')),max_length=30,verbose_name='验证码类型')
    send_time = models.DateTimeField(default=datetime.now,verbose_name='发送时间')

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}({1})'.format(self.code,self.email)

#轮播图
class Banner(models.Model):
    title = models.CharField(max_length=100,verbose_name='标题')
    image = models.ImageField(upload_to='banner/%Y/%m',verbose_name='轮播图',max_length=100)
    url = models.URLField(max_length=200,verbose_name='访问地址')
    index = models.IntegerField(default=100,verbose_name='顺序')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name