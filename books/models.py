from django.db import models

class Books(models.Model):
       title = models.CharField(max_length=100,verbose_name='название',unique=True)
       description = models.TextField(max_length=1000,verbose_name='описании',blank=True)
       owner = models.CharField(max_length=10,verbose_name='автор книги')

       def __str__(self):
           return self.title




