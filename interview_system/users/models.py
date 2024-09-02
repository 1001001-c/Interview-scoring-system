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
        ('candidate', '考生')
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    # 解决冲突：指定不同的 related_name
    groups = models.ManyToManyField(Group, related_name='userprofile_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='userprofile_permissions')



class Candidate(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    full_name = models.CharField(max_length=255)
    id_number = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    # 其他相关字段

    def __str__(self):
        return self.full_name
