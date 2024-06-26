from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from typing import Any
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, get_user_model, logout
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse_lazy

from .models import ProductModel, CategoryModel
from .forms import SignUpForm, ProductsForm


# #Generic signup
class SignUpView(CreateView):
    model=get_user_model
    template_name="blogs/signup.html"
    form_class=SignUpForm
    success_url=reverse_lazy("blogs:login")

    def form_valid(self, form):
        messages.success(self.request,"account has been created")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,"failed to create account")
        return super().form_invalid(form)

        
# login method-2
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        print(username)
        print(password)
        
        if user is not None:
            login(request,user)
            print('user not none')
            return HttpResponseRedirect('/products/')

            # return render(request, 'blogs/products.html',{'is_admin':is_admin})
            # return redirect('/products/?is_admin={}'.format(is_admin))
            # return reverse_lazy(redirect ('products/', {'is_admin':is_admin}))
            # return HttpResponseRedirect('/products/')
        else:
            print('user none')
            messages.error(request, 'Invalid username or password.')
            return HttpResponseRedirect('/')
    else:
        print('back to the start')
        form = AuthenticationForm()
        # If it's a GET request, display the login form
        return render(request, 'blogs/login.html',{'form':form}) 

# @login_required  
def product_list_by_category(request):
    categories = CategoryModel.objects.all()
    category_product_map = {}

    for category in categories:
        products = ProductModel.objects.filter(category=category).order_by('price')
        category_product_map[category] = products

    return render(request, 'blogs/products.html', {'category_product_map': category_product_map})





class AddprodView(LoginRequiredMixin, CreateView):
    template_name= "blogs/addproduct.html"
    context_object_name='products'
    model=ProductModel
    form_class=ProductsForm
    success_url=reverse_lazy('blogs:products')

    def form_valid(self, form):
        print('successful post')
        return super().form_valid(form)

    def form_invalid(self, form):
        print('post method failed')
        return super().form_invalid(form)


# #Generic signup
class SpecView(CreateView):
    model=get_user_model
    template_name="blogs/productspec.html"
    form_class=SignUpForm
    success_url=reverse_lazy("blogs:login")

    def form_valid(self, form):
        messages.success(self.request,"account has been created")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,"failed to create account")
        return super().form_invalid(form)


def sign_out(request):
    logout(request)
    return HttpResponseRedirect('/')  # Redirect to the login page




#Better code to fetch products acc. to category without multiple database queries
#Use django's prefetch_related or select_related
#Here the problem is that the returned dictionary is a list of category sorted based on the price of the items.
#We actually need a list of products filtered by price. For that the 'categories_with_products' need to be filtered based on category and the order by price.
#Code need to be modified
    
# @login_required
# def product_list_by_category(request):
#     try:
#         # Retrieve all categories with related products ordered by price
#         categories_with_products = CategoryModel.objects.prefetch_related('productmodel_set').order_by('productmodel__price')
#     except CategoryModel.DoesNotExist:
#         # Handle the case where no categories are found
#         categories_with_products = []

#     return render(request, 'blogs/products.html', {'categories_with_products': categories_with_products})





# class ProductView(ListView):
#     template_name= "blogs/products.html"
#     context_object_name='products'

#     def get_queryset(self):
#         return ProductModel.objects.all()




# class ProductView(ListView):
#     model=ProductModel
#     template_name= "blogs/products.html"
#     context_object_name='products'

# def prodView(request):
#         is_admin = request.GET.get('is_admin')
#         print(is_admin)
#         # Pass the is_admin value to the HTML template
#         return render(request, 'blogs/products.html', {'is_admin': is_admin})



# class ProductView(ListView):
#     model=ProductModel
#     template_name= "blogs/products.html"
#     context_object_name='products'

#     # def prodView(request):
#     #     is_admin=request.GET.get('is_admin')

#     def get_context_data(self,**kwargs):
       
#         context = super().get_context_data(**kwargs)
#         # context['is_admin']= is_admin
#         context['products'] = ProductModel.objects.all()
#         # print(is_admin)
        
#         return context
    









#class Feed_inputView(CreateView, ListView):
#     model=PostModel
#     form_class=PostForm
#     template_name= "blogs/homegeneric.html"
#     context_object_name = "feeds"

#     def get_queryset(self):
#         return PostModel.objects.all()
    
#     def form_valid(self, form):
#         return super().form_valid(form)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['form'] = self.get_form()
    #     return context






    
# #Generic view of feed_input
# class feed_inputView(generic.DetailView):
#     model = PostModel
#     form_class = PostForm
#     template_name = 'blogs/home.html'
#     success_url = reverse('home')

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['feeds'] = PostModel.objects.all()
#         return context

# def feeds(request):
#     data = FeedModel.objects.all()
#     users = User.objects.all()
#     return render(request, 'blogs/feeds.html', {'data':data, 'users':users})


# def index(request):
#     return render(request, "blogs/signup.html")
    

# def signup(request):
#     if request.method == 'POST':
#         print('post method')
#         form = SignUpForm(request.POST)
        
#         if form.is_valid():
#             print('valid form')
#             form.save()
#             return HttpResponseRedirect('/login') # Redirect to success page after signup
#     else:
#         print('method not detected')
#         form = SignUpForm()
#     return render(request, 'blogs/signup.html', {'form': form})
    



    # class ProductView(ListView):
#     template_name= "blogs/products.html"
#     context_object_name='products'
    
#     def get_queryset(request,self,*args, **kwargs):
#         is_admin=self.user.is_staff
#         return render(request,self.template_name,{'is_admin':is_admin})



#With the following code, on successful login redirects to /products/ url but "is_admin" value (context)-
    #is not passed to conditionally render products page with "Add Product" button for admin
# # login method-2
# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
        
#         user = authenticate(request, username=username, password=password)
#         print(username)
#         print(password)
        
#         if user is not None:
#             login(request, user)
#             print('user not none')
#             is_admin=request.user.is_staff
#             return HttpResponseRedirect('/products/')
        
#             # return reverse_lazy(redirect ('products/', {'is_admin':is_admin}))
#             # return HttpResponseRedirect('/products/')
#         else:
#             print('user none')
#             messages.error(request, 'Invalid username or password.')
#             return HttpResponseRedirect('/login')
#     else:
#         print('back to the start')
#         form = AuthenticationForm()
#         # If it's a GET request, display the login form
#         return render(request, 'blogs/login.html',{'form':form}) 
    

#This product view also need to be modified as above to get the context data ("is_admin") to conditionally render products page with "Add Product button"
# class ProductView(ListView):
#     model=ProductModel
#     template_name= "blogs/products.html"
#     context_object_name='products'

#     def get_context_data(self,**kwargs):
#         context = super().get_context_data(**kwargs)

#         context['is_admin']='is_admin'
#         return 
    