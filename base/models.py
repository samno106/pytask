from django.db import models

# Create your models here.
class Task(models.Model):
    class TaskStatus(models.TextChoices):
        PENDING = "PENDING"
        PROGRESS = "PROGRESS"
        COMPLETED = "COMPLETED"
    title =models.CharField(max_length=255)
    desc = models.TextField()
    status= models.CharField(max_length=20,choices=TaskStatus.choices,default=TaskStatus.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"
   
