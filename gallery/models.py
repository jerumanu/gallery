from django.db import models
import datetime as dt

from cloudinary.models import CloudinaryField
# Create your models here.


class Image(models.Model):
    title = models.CharField(max_length =60)
    Category = models.TextField()
    image=CloudinaryField('image')
    description=models.TextField()
    location = models.TextField(max_length=30 ,default = '')
    date_created = models.DateTimeField(auto_now_add=True, null = True)
    
    
    def __str__(self):
        return self.description

    class Meta:
        verbose_name='Images'


    @classmethod
    def search_by_title(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return news
    
class Category(models.Model):
    category = models.CharField(max_length=80, null= True)
    
    def save_category(self):
        self.save()
    def delete_category(self):
        self.delete()
    def update_category(self):
        self.update()
    def __str__(self):
        return self.category
        
class Categories(models.Model):
    name = models.CharField(max_length=30)
    def save_category(self):
        self.save()
    def delete_category(self):
        self.delete()
    def __str__(self):
        return self.name
    
class Location(models.Model):
    name = models.CharField(max_length=30)
    def save_location(self):
        self.save()
    def delete_location(self):
        self.delete()
    def __str__(self):
        return self.name
    