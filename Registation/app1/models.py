from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class BMI(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    weight = models.FloatField()
    height = models.FloatField()
    bmi = models.FloatField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username
