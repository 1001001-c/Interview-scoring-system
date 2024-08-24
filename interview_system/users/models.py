from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser, Group, Permission

class UserProfile(AbstractUser):
    ROLE_CHOICES = [
        ('admin', '管理员'),
        ('chief_examiner', '主考'),
        ('assistant_examiner', '辅考'),
        ('exam_staff', '考务'),
        ('evaluator', '评委'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    # 其他字段...

    # 解决冲突：指定不同的 related_name
    groups = models.ManyToManyField(Group, related_name='userprofile_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='userprofile_permissions')