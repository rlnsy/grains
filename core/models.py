from django.db import models

class Project(models.Model):

	descriptor = models.CharField('name/description', max_length=200)
	project_tag = models.CharField('tag', max_length=100)
	init_date = models.DateTimeField('date created')

	def __str__(self):
		return self.descriptor