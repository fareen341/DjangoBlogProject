from django.db import models
import datetime

# Create your models here.
class Blog(models.Model):
    featured_image = models.ImageField(upload_to='images')
    tag=models.CharField(max_length=40)
    title=models.CharField(max_length=800)
    content=models.TextField()
    date=models.DateField(default=datetime.datetime.now())
    author = models.CharField(max_length=30)
    slug=models.SlugField(max_length=40, unique=True, verbose_name="Blog Url", help_text="Url of the blog")
    code=models.TextField(null=True, blank=True)

# featured image
# tag
# title
# content
# written by
# date