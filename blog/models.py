from django.db import models

# Create your models here.
class Post(models.Model):
 title = models.CharField(max_length=150)
 desc = models.TextField()
 user=models.CharField(max_length=200)



#model for contact form

class ContactForm(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    address=models.TextField()
    message=models.TextField()
