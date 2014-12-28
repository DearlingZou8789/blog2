from django.db import models

sex_choices=(
        ('f','female'),
        ('m','male'),
    )
# Create your models here.
class Entry(models.Model):
    name=models.CharField(max_length=30)
    sex=models.CharField(max_length=1,choices=sex_choices)
    def __unicode__(self):
        return self.name

class Blog(models.Model):
        name=models.CharField(max_length=30)
        entry=models.ForeignKey(Entry)

        def __unicode__(self):
            return self.name

class Author(models.Model):
    name=models.CharField(max_length=38)

    def __unicode__(self):
            return self.name

class Book(models.Model):
    name=models.CharField(max_length=100)
    authors=models.ManyToManyField(Author)
    
    def __unicode__(self):
        return self.name

class User(models.Model):
	name=models.CharField(max_length=100)
	headimage=models.FileField(upload_to="./upload/")

	def __unicode__(self):
		return self.name
