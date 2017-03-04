from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.

class User(models.Model):
	email = models.CharField(max_length=500)
	model_name = models.CharField(max_length=500)
	model_number = models.CharField(max_length = 10)
	size = models.CharField(max_length = 10)

	def get_absolute_url(self):
		return reverse('detail')

	def __str__(self):
		return self.email + ' - ' + self.model_name + ' - ' + self.size




