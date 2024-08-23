from django.db import models
from exams.models import ExamRoom, ScoreItem
from users.models import UserProfile

# Create your models here.

class Score(models.Model):
    exam_room = models.ForeignKey(ExamRoom, on_delete=models.CASCADE)
    candidate = models.ForeignKey(UserProfile, on_delete=models.CASCADE)  # 考生
    score_item = models.ForeignKey(ScoreItem, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=5, decimal_places=2)
    # 其他字段...
