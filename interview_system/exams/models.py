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

class Exam(models.Model):
    exam_name = models.CharField(max_length=255)
    num_exams = models.PositiveIntegerField()
    judges_range = models.CharField(max_length=50)  # 可以存储例如 "3-5" 这样的字符串
    students_per_round = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.exam_name

class ExamPosition(models.Model):
    exam = models.ForeignKey(Exam, related_name='exam_positions', on_delete=models.CASCADE)
    code = models.CharField(max_length=100)
    questions = models.TextField(help_text='用逗号分隔的问题列表')

    def __str__(self):
        return self.code

class ScoringItem(models.Model):
    exam = models.ForeignKey(Exam, related_name='scoring_items', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    criteria = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
