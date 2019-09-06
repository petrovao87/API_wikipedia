from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class Note(models.Model):
    title = models.CharField(db_index=True, max_length=55)
    url = models.CharField(max_length=1000)
    content = models.CharField(max_length=10000)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
