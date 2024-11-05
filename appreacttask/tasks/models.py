from django.db import models

# Create your models here.
class Task(models.Model):
    class Meta:
        db_table = 'tasks'

    title = models.CharField(max_length=200)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    author = models.IntegerField(null=True)

    def __str__(self): 
        return self.title
