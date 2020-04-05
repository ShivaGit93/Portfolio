from django.db import models

class Blog(models.Model):
    titles=models.CharField(max_length=200)
    pub_date=models.DateTimeField()
    body=models.TextField()
    image=models.ImageField(upload_to='image/')

