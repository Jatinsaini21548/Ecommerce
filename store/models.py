from django.db import models
import datetime
import os
from django.contrib.auth.models import AbstractUser

class Register_user(AbstractUser):
    token =  models.IntegerField(null=True)
    address = models.CharField(max_length = 450, null=True)
    optional_address = models.CharField(max_length=450, null=True) 
    country = models.CharField(max_length = 50, null=True)
    state = models.CharField(max_length = 50, null=True)
    zip = models.IntegerField(null=True, blank = False)

def get_file_path(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (nowTime, original_filename)
    return os.path.join('uploads/', filename) 



class Category(models.Model):
    slug = models.CharField(max_length = 50, null = False, blank = False)
    name = models.CharField(max_length = 150 , null = False, blank = False)
    image = models.ImageField(upload_to = get_file_path, null=True , blank=True)
    description = models.TextField(max_length=500, null = False , blank= False)
    status = models.BooleanField(default = False, help_text="0= default, 1= Hidden")
    trending = models.BooleanField(default = False, help_text="0= default, 1= Trending")
    meta_title = models.CharField(max_length = 150, null = False, blank = False)
    meta_keywords = models.CharField(max_length = 150, null = False, blank = False)
    meta_description = models.TextField(max_length = 500, null = False, blank = False)
    created_at = models.DateTimeField(auto_now= True)


    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    slug = models.CharField(max_length = 50, null = False, blank = False)
    name = models.CharField(max_length = 150 , null = False, blank = False)
    product_image = models.ImageField(upload_to = get_file_path, null=True , blank=True)
    small_descriptiom = models.CharField(max_length=150 ,null=False, blank= False)
    quantity = models.IntegerField(null=False)
    description = models.TextField(max_length = 500, null = False , blank= False)
    original_price = models.FloatField(null = False, blank = False)
    selling_price = models.FloatField(null = False, blank = False)
    status = models.BooleanField(default = False, help_text="0= default, 1= Hidden")
    trending = models.BooleanField(default = False, help_text="0= default, 1= Trending")
    tag = models.CharField(max_length = 50, null = False, blank = False)
    meta_title = models.CharField(max_length = 150, null = False, blank = False)
    meta_keywords = models.CharField(max_length = 150, null = False, blank = False)
    meta_description = models.TextField(max_length = 500, null = False, blank = False)
    created_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.name
    

class Cart(models.Model):
    user = models.ForeignKey(Register_user, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE )
    product_qty = models.IntegerField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add= True)



class BillingDetail(models.Model):
    first_name = models.CharField(max_length = 60)
    last_name = models.CharField(max_length = 60)
    email = models.EmailField()





