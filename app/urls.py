from django.urls import path

from app.views import index, product_detels, order_list, customer_list, order_details, add_product, \
    add_user, user_settings, update_user_settings, user_profile, category, add_category, customer_add, customer_delete, \
    customer_details, customer_update, login

urlpatterns = [
    path('add-user', add_user, name='add_user'),
    path('update-settings', update_user_settings, name='update_user_settings'),
    path('user-settings/<int:user_id>', user_settings, name='user_settings'),
    path('user-profile/<int:user_id>', user_profile, name='user_profile'),
    # path('user-update/<int:user_id>', user_update, name='user_update'),

    path('category', category, name='category'),
    path('category/<str:category_slug>', index, name='category_by_slug'),
    path('add-category', add_category, name='add_category'),

    path('', index, name='index'),
    path('add-product', add_product, name='add_product'),
    path('product_detels/<int:product_id>', product_detels, name='product_detels'),
    path('order_list', order_list),
    path('order_details', order_details),
    path('customer-list', customer_list , name = 'customers'),
    path('customers-add' , customer_add , name= 'costumer_add'),
    path('customers-details/<int:customer_id>' , customer_details , name= 'customer_details'),
    path('customers-delete/<int:customer_id>' , customer_delete , name= 'customer_delete'),
    path('customers-update/<int:customer_id>' , customer_update , name= 'customer_update'),
    path('login-page' , login , name= 'login_page')

]
