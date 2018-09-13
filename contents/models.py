from django.conf import settings
from django.db import models


class DjangoUser(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
    null=True)
    name = models.CharField(max_length=100)
    profile = models.URLField()

    def __str__(self):
        return self.name


class Company(models.Model):
    CATEGORY_CHOICES = (
        ('fi', '핀테크'),
        ('so', '소셜'),
        ('ec', '전자상거래'),
        ('ft', '푸드테크'),
    )

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    url = models.URLField()
    job = models.URLField()

    def __str__(self):
        self.name


class Community(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        self.name


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField()

    def __str__(self):
        self.name


class Archive(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    url = models.URLField() 

    def __str__(self):
        self.title