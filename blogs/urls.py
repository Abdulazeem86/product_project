from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = "blogs"
urlpatterns = [
   
    path('', views.SignUpView.as_view(), name='signup'),
    path('home/', views.feed_input, name="home"),
    path('login/', views.user_login, name="login"),
    path('feed/',views.FeedView.as_view(), name='feed'),
    path('homegeneric/', views.FeedInputView.as_view(), name='homegeneric'),
    path('products/', views.product_list_by_category, name='products'),
    path('addproduct/', views.Addprodview.as_view(), name='addproduct')
   ]