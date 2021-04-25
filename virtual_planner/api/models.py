from django.db import models

#Creates object models
class Goal(models.Model):
    text = models.CharField(max_length = 1000, null=False)
    due_date = models.DateField()
    goal_type = models.CharField(max_length = 200, null=False) #weekly or monthly
    completed = models.BooleanField(default = False)

    def __string__(self):
        return self.text

class Work(models.Model):
    text = models.CharField(max_length = 1000, null=False)
    due_date = models.DateField()
    work_type = models.CharField(max_length=200) #daily or after_school
    completed = models.BooleanField(default = False)

    def __string__(self):
        return self.text
