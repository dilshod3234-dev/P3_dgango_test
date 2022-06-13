from django.http import HttpResponse
from django.shortcuts import render, redirect

# Product list
from app.forms import ProductModelForm, UserModelForm, CategoryModelFrom, CustomerModelFrom
from app.models import Product, User, Category, Customers


# Home task
# ================add users=========================
def add_user(request):
    user_form = UserModelForm()

    if request.method == 'POST':
        user_form = UserModelForm(request.POST)
        if user_form.is_valid():
            user_form.save(commit=True)

        return redirect('update_user_settings')

    context = {
        'form': user_form
    }
    return render(request, 'app/add_user.html', context=context)

# TODO def update_user(request , user_id):



def user_settings(request, user_id):
    users = User.objects.filter(id=user_id)[0]

    context = {
        'user': users
    }
    return render(request, 'app/user-settings.html', context=context)


def update_user_settings(request):
    users = list(User.objects.all())[-1]

    context = {
        'user': users
    }
    return render(request, 'app/user-settings.html', context=context)


def user_profile(request, user_id):
    users = User.objects.filter(id=user_id)[0]

    context = {
        'user': users
    }
    return render(request, 'app/profile.html', context=context)


# category
def category(request):
    category_products = Category.objects.filter(parent__isnull= True)

    context = {
        'category_products': category_products
    }
    return render(request, 'app/category-page.html', context=context)


def add_category(request):
    category_form = CategoryModelFrom()

    if request.method == 'POST':
        user_form = CategoryModelFrom(request.POST)
        if user_form.is_valid():
            user_form.save(commit=True)

        return redirect('category')

    context = {
        'form': category_form
    }
    return render(request, 'app/add-category.html', context=context)


# ==================================================


def index(request , category_slug = None):
    if category_slug:
        product = Product.objects.filter(category__slug = category_slug)
    else:
        product = Product.objects.all()
    content = {
        'product': product
    }
    return render(request, 'app/index.html', context=content)


def add_product(request):
    product_form = ProductModelForm()

    if request.method == 'POST':
        form = ProductModelForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return redirect('index')

    context = {
        'form': product_form
    }

    return render(request, 'app/add_product.html', context=context)


# Product delete
def product_delete(request):
    return render(request, 'app/index.html')


# Product_detals
def product_detels(request, product_id):
    product = Product.objects.filter(id=product_id)[0]
    content = {
        'product': product
    }
    return render(request, 'app/product_detels.html', context=content)


# customers
def customer_list(request):
    customers = Customers.objects.all()

    context = {
        'customers': customers
    }

    return render(request, 'app/customers.html', context=context)


def customer_add(request):
    customer_form = CustomerModelFrom()

    if request.method == 'POST':
        form = CustomerModelFrom(request.POST)

        if form.is_valid():
            form.save(commit=True)

        return redirect('customers')

    context = {
        'forms': customer_form
    }

    return render(request, 'app/add-customers.html', context=context)


def customer_details(request, customer_id):
    customer = Customers.objects.filter(id=customer_id)[0]

    context = {
        'customer': customer
    }
    return render(request, 'app/cutomer-details.html', context=context)


def customer_delete(request, customer_id):
    customer = Customers.objects.filter(id=customer_id).first()

    if customer:
        customer.delete()

    return redirect('customers')





def customer_update(request, customer_id):
    customer = Customers.objects.filter(id=customer_id).first()

    if request.method == 'POST':
        form = CustomerModelFrom(request.POST, instance=customer)
        if form.is_valid():
            form.save()
        return redirect('customers')
    else:
        form = CustomerModelFrom(instance=customer)
        context = {
            'form': form
        }
        return render(request, 'app/customer-update.html', context=context)


# order_list
def order_list(request):
    return render(request, 'app/order_list.html')


# order_list
def order_details(request):
    return render(request, 'app/order_details.html')



def login(request):
    return render(request , 'app/auth/login.html')

