from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Blogpost(models.Model):
    title = models.CharField(max_length=20)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, True)

    def __str__(self):
        return self.title + '(' + str(self.date_added) + ')'
