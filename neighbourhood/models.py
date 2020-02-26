from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Neighbourhood(models.Model):
    neighborhood_name = models.CharField(max_length =30)
    location = models.CharField(max_length =30)
    house_number =  models.IntegerField(default=0)
    #admin foreging key
    def __str__(self):
        return self.neighborhood_name

        
class Profile(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    username = models.CharField(max_length =30)
    identification_card =  models.IntegerField(default=0)
    neighborhood = models.ForeignKey(Neighbourhood)
    bio = models.TextField()
    email = models.EmailField()
    contact =  models.IntegerField(default=0)
    #profile_image = models.ImageField(upload_to = 'profiles/')
    def __str__(self):
        return self.username

    def save_profile(self):
        self.save()

class Business(models.Model):
    business_name = models.CharField(max_length =30)
    business_descrpition = models.TextField()#spellin error
    user = models.ForeignKey(Profile)
    neighborhood = models.ForeignKey(Neighbourhood)
    business_email = models.EmailField()
    def __str__(self):
        return self.business_name

    @classmethod
    def search_business(cls,search_term):
        business = cls.objects.filter(business_name__icontains=search_term)
        return business

        
class Posts(models.Model):
    message=HTMLField()
    pub_date = models.DateTimeField(auto_now_add=True)
    #message_image = models.ImageField(upload_to = 'posts/')
    name=models.ForeignKey(User,on_delete=models.CASCADE)
    
    @classmethod
    def show_posts(cls):
        posts= cls.objects.order_by('-pub_date')
        return posts