from django.db import models

# Create your models here.


class TaskModel(models.Model):
    ID = models.IntegerField(primary_key=True)
    Task_Title = models.CharField(max_length=50)
    Task_Description = models.TextField()
    Status = models.BooleanField(default=False)

    def status_display(self):
        return "Complete" if self.Status else "Incomplete"
