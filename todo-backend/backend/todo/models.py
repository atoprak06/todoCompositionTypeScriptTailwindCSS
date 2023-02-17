from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    stateChoices = (('important','Important'),('dontForget','Dont Forget'))
    state = models.CharField(max_length=40,choices=stateChoices,default='important')
    isChecked=models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
