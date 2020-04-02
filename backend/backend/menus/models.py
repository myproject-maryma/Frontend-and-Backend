from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Menus(models.Model):
    user = models.ForeignKey(User, related_name='menus', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'menus'

    def __str__(self):
        return self.name
