from django.contrib import admin
from .models import User, ProductModel,CategoryModel

# Register your models here.
admin.site.register(User),
admin.site.register(ProductModel),
admin.site.register(CategoryModel),