from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Term(models.Model):
    value = models.CharField(max_length=45)
    count = models.IntegerField(default=0)
    def __str__(self):
        return self.value

