from django.db import models

# Create your models here.
class Blog(models.Model):
	blog_image = models.ImageField(upload_to='blog_images/')
	blog_text = models.TextField()
	blog_title = models.CharField(max_length=300)
	blog_date = models.DateTimeField()