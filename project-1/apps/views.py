from django.contrib.auth import login,logout

from django.shortcuts import render,redirect

from django.views.generic import (
    TemplateView, ListView,
    DetailView, CreateView,
    DeleteView, UpdateView, FormView,View
)

from apps.models import Product, User

from .forms import UserRegisterForm, UserLoginForm


class ProductListView(ListView):
    model = Product
    template_name = 'product/product-grid.html'
    context_object_name = 'products'
    # ordering = ['-created_at']


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product-details.html'
    context_object_name = 'product'


class ProfileView(TemplateView):
    model = User
    template_name = 'user/profile.html'
    context_object_name = 'user'
    
    def get_context_data(self, **kwargs):
       data = super().get_context_data(**kwargs)
       user = self.request.user
       data['user'] = user
       return data


class SettingsView(TemplateView):
    template_name = 'user/settings.html'


class UserRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'auth/register.html'
    success_url = '/'


class UserLoginView(FormView):
    form_class = UserLoginForm
    template_name = 'auth/login.html'
    success_url = '/'

    def form_valid(self, form):
        # print("Ishlayabdi")
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = User.objects.filter(username=username).first()
        print(username, password, user)
        if user and user.check_password(password):
            login(self.request, user)
        return super().form_valid(form)

    def form_invalid(self, form):
        # print('Ishlamayabdi')
        return super().form_invalid(form)


class UserLogoutView(View):
    def get(self,request,*args, **kwargs):
        logout(self.request)
        return redirect('/')



