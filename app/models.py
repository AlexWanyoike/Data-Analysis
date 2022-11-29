from django.db import models
import datetime as dt
# Create your models here.


class Analysis(models.Model):
    model = models.CharField(max_length=30)
    models  = models.CharField(max_length=30)

    def __str__(self):
        return self.name

