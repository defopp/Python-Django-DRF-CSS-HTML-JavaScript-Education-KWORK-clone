from django.db import models
from usersApp.models import User
# from django.contrib.auth import get_user_model
# User = get_user_model() 

# Create your models here.
class MainCategory(models.Model):
    name = models.CharField(max_length = 50, blank = False, unique = True)
    urlname = models.CharField(max_length = 20, blank = False)
    description = models.CharField(max_length = 100, blank = True)
    
    def __str__(self):
        return self.name
    
class SubCategory(models.Model):
    main_category = models.ForeignKey(MainCategory, on_delete=models.PROTECT)
    name = models.CharField(max_length = 50, blank = False, unique = True)
    urlname = models.CharField(max_length = 20, blank = False)
    
    def __str__(self):
        return self.name
    
class DetailCategory(models.Model):
    sub_category = models.ForeignKey(SubCategory, on_delete=models.PROTECT)
    name = models.CharField(max_length = 50, blank = False, unique = True)
    urlname = models.CharField(max_length = 20, blank = False)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    sell_type = models.BooleanField(blank=False)
    name = models.CharField(blank=False, max_length=150, null=False)
    description = models.CharField(blank=False, max_length=1500, null=False)
    main_cat = models.ForeignKey(MainCategory, to_field="name", on_delete=models.PROTECT,)
    sub_cat = models.ForeignKey(SubCategory, to_field="name", on_delete=models.PROTECT,)
    detail_cat = models.ForeignKey(DetailCategory, to_field="name", on_delete=models.PROTECT,)
    price = models.IntegerField(blank=False, null=False)
    
    def __str__(self):
        return f"{self.id}.{self.name}"