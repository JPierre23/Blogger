from datetime import datetime
from statistics import mode
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.


class Tags(models.Model):
    tag=models.CharField(max_length=50)

    def __str__(self):
        return '#'+self.tag

    def get_absolute_url(self):
        return reverse('tag',kwargs={'tag_id':self.id})
    

class Blog(models.Model):
    
    title=models.CharField(max_length=100)
    img=models.CharField(max_length=250)
    date=models.DateField('Date',default=datetime.now)
    # tags=models.ManyToManyField(Tags)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    info=models.CharField(max_length=2000)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog', kwargs={'blog_id': self.id})
    
    
class Comment(models.Model):
    date=models.DateField('Date',default=datetime.now)
    comment=models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog= models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}: {self.commment} "