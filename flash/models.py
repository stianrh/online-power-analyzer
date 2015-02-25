from django.db import models
from filer.fields.file import FilerFileField
import subprocess

# Create your models here.

class FlashManager(models.Manager):
    def create_new(self):
        q = Flash()
        q.save()
        return q

class Flash(models.Model):

    main_dir = models.FilePathField(path='/home/devzone/sdk7.2/examples')
    defines = models.CharField(max_length=200, default='')


    objects = FlashManager()

    def __unicode__(self):
        return self.id

    def compile(self):
        cmd = 'make -C /home/devzone/sdk7.2/examples/ble_peripheral/ble_app_beacon/pca10028/s110/armgcc/'
        p = subprocess.Popen(cmd, shell=True)

