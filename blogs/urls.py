from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = "blogs"
urlpatterns = [
    path('', views.user_login, name="login"),
   
    path('signup/', views.SignUpView.as_view(), name='signup'),
             
    path('products/', views.product_list_by_category, name='products'),
    
    path('addproduct/', views.AddprodView.as_view(), name='addproduct'),

    path('productspec/', views.SpecView.as_view(), name='productspec'),

    path('signout/', views.sign_out, name='signout')
   ]