from django.forms import ModelForm

from app.models import Product, User, Category, Customers


class ProductModelForm(ModelForm):
    class Meta:
        model = Product
        exclude = ()


class UserModelForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name',
                  'last_name',
                  'email',
                  'phone',
                  'heading',
                  'intro'
                  ]


class CategoryModelFrom(ModelForm):
    class Meta:
        model = Category
        fields = [
                  'image',
                  'name',
                  ]

class CustomerModelFrom(ModelForm):
    class Meta:
        model = Customers
        fields = [
            'name',
            'email',
            'phone'
        ]
