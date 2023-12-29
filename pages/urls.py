from django.urls import path
from .views import index , contact, product_details, shop, SignUpView
app_name = 'pages'
urlpatterns = [
    path('', index, name='home'),
    path('contact', contact, name='contact'),
    path('shop', shop, name='shop'),
    path('product-details/', product_details, name='product-details'),
    path('signup/', SignUpView.as_view(), name='signup')

]