from django.db import models

# Create your models here.
class ExamProject(models.Model):
    name = models.CharField(max_length=100)
    exam_rooms = models.IntegerField()
    position_code = models.CharField(max_length=20)
    # 其他字段...

class ExamRoom(models.Model):
    project = models.ForeignKey(ExamProject, on_delete=models.CASCADE)
    min_examiners = models.IntegerField()
    max_examiners = models.IntegerField()
    # 其他字段...

class ScoreItem(models.Model):
    project = models.ForeignKey(ExamProject, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=5, decimal_places=2)
    # 其他字段...
