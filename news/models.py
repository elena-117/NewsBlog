from django.db import models
import datetime

# Create your models here.

class Articles(models.Model):
    """Class representing an article"""
    title = models.CharField('Caption', max_length=50)
    preview = models.CharField('Preview', max_length=250)
    full_text = models.TextField('Article')
    date = models.DateField('Posting date')
    time = models.TimeField('Posting time', default=datetime.time(16, 00))

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/news/{self.id}'
    
    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'