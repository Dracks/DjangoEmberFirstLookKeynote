from django.db import models

# Create your models here.

class SampleModel(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name