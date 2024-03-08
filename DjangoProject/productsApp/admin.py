from django.contrib import admin

from .models import MainCategory, SubCategory, DetailCategory, Product

# Register your models here.
admin.site.register(MainCategory)
admin.site.register(SubCategory)
admin.site.register(DetailCategory)
admin.site.register(Product)