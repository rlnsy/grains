from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):

    descriptor = models.CharField('name/description', max_length=200)
    project_tag = models.CharField('tag', max_length=100)
    init_date = models.DateTimeField('date created')
    creator = models.CharField('creator', max_length=100)

    def __str__(self):
        return self.descriptor


class UserProxy(User):
    class Meta:
        proxy = True

    def get_projects(self):
        projects = Project.objects.filter(creator=self.username)
        return projects