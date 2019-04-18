from django.db import models


class YumPackages(models.Model):
    name = models.CharField(max_length=128)
    packages = models.CharField(max_length=2048)
    releasever = models.CharField(max_length=128)
    repo_name = models.CharField(max_length=128)
