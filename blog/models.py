from django.db import models

class Blog(models.Model):
    titles=models.CharField(max_length=200)
    pub_date=models.DateTimeField()
    body=models.TextField()
    image=models.ImageField(upload_to='image/')

    def __str__(self):
        return self.titles

    def summary(self):
        return self.body[:1000]
    def pub_date_modified(self):
        return self.pub_date.strftime(' %b %e %Y')

