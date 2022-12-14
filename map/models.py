from enum import auto
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Search(models.Model):
    address = models.CharField(max_length = 255, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
