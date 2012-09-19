from django.db import models
from django.utils import timezone
import datetime
# Create your models here.

class userData(models.Model):
	name = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	def __unicode(self):
		return self.name

class content(models.Model):
	user = models.ForeignKey(userData)
	created = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=100)
	content = models.CharField(max_length=10000)
	def __unicode(self):
		return self.title
