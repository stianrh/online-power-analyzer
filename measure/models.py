from django.db import models

class MeasureManager(models.Manager):
    def start(self):
        q = Measure()
        q.save()
        return q

        return self.get_db_prep_value(value)

class Measure(models.Model):
    voltage = models.FloatField(default=2.8)
    time = models.IntegerField(default=10)
    resolution = models.IntegerField(default=1000)
    measure_list = models.TextField(default='None') 
    average = models.FloatField(default=0)


    objects = MeasureManager()

    def __unicode__(self):
        return self.id
