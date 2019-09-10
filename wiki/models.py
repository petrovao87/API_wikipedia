from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.


class Note(models.Model):
    title = models.CharField(db_index=True, unique=True,  max_length=55)
    url = models.CharField(unique=True, max_length=250)
    content = models.TextField(null=True)
    categories = models.TextField(default='No categories')
    links = models.TextField(default='No links')
    images = models.TextField(default='No images')

    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return '%s, %s' % (self.title, self.url)
