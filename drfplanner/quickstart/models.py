from django.db import models

class Goal(models.model):
    goal_type = models.CharField(max_length=60)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text
