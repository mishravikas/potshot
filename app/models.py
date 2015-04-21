from django.db import models
import os
import uuid
from django.conf import settings

# Create your models here.
def get_image_path(self, filename): 

    f, ext = os.path.splitext(filename)
    name = "%s%s" % (uuid.uuid4(), ext)
    return "%s" %(name)

class Comic(models.Model):      
    title = models.CharField(max_length=128, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to=get_image_path)

    def __unicode__(self):
        return u'%d: %s' % (self.id, self.title)

class Contact(models.Model):
	name = models.CharField(max_length=32,blank=False)
	email = models.CharField(max_length=64,blank=False)
	subject = models.CharField(max_length=256,blank=False)
	message = models.CharField(max_length=1024,blank=False)
