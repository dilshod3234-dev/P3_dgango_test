from datetime import timezone

from django.core.validators import integer_validator
from django.db.models import (
    Model, CharField, FloatField, IntegerField, ImageField, CASCADE, ForeignKey, EmailField, DateTimeField, SET_NULL,
    SlugField)


# Home task
# ====================================
from django.template.defaultfilters import slugify


class User(Model):
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    email = CharField(max_length=255)
    phone = IntegerField()
    # from_ = CharField(max_length=255)
    heading = CharField(max_length=255)
    intro = CharField(max_length=10000)

class ImageUser(Model):
    image = ImageField(upload_to='users/')
    user = ForeignKey('app.User', CASCADE)




class Product(Model):
    title = CharField(max_length=255)
    category = ForeignKey('app.Category' , SET_NULL ,blank=True , null=True )
    price = FloatField()
    description = CharField(max_length=1000, blank=True, null=True)
    amount = IntegerField(default=1)

    def __str__(self):
        return self.title

class Category(Model):
    parent = ForeignKey('app.Category' , SET_NULL , blank=True , null=True)
    image = ImageField(upload_to='category/')
    name = CharField(max_length=255)
    slug = SlugField(unique=True )

    def __str__(self):
        return self.name


    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.slug:
            self.slug = slugify(self.name)
            while Category.objects.filter(slug=self.slug).exists():
                self.slug = f'{self.slug}-1'

        super().save(force_insert, force_update, using, update_fields)



class Image(Model):
    image = ImageField(upload_to='products/')
    product = ForeignKey('app.Product', CASCADE)



class Customers(Model):
    name = CharField(max_length=255, null = True)
    email = EmailField(max_length=255)
    phone = CharField(max_length=255, validators=[integer_validator])

    update_at = DateTimeField(auto_now = True)
    create_at = DateTimeField(auto_now_add = True)



