from django.db import models

# Create your models here.


class Tag(models.Model):
    models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return self.name


class Link(models.Model):
    title = models.CharField(max_length=128, unique=True)
    url = models.URLField(max_length=128, unique=True)
    # Many to many foreign key
    tags = models.ManyToManyField(Tag)

    def __unicode__(self):
        return self.title
