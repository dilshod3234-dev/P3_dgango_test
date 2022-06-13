from django.contrib import admin

from app.models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id' ,'title' , 'price' ,'amount' ]
    # fields = ['title','category','price', 'description', 'amount']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'slug']
    fields = ['image', 'name']




