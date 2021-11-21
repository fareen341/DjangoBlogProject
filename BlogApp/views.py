from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.views.generic.base import View
from .models import Blog
from .forms import BlogForm
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib import messages
from django.views.generic.edit import DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def BaseView(request, template_name):
    t=template_name
    blog=Blog.objects.all()
    return render(request,t ,{'blog':blog})

def About(request):
    return render(request, "about.html")

def Author(request):
    return render(request, "author.html")


def Loginuser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        #check if user has correct credential
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # A backend authenticated the credentials
            return redirect("/")
        else:
            # No backend authenticated the credentials
            return render(request,'login.html')
    return render(request,'login.html')

def Logoutuser(request):
    logout(request)
    return redirect("/about/")

class BlogCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model=Blog
    form_class = BlogForm			
    template_name = "addblog.html"
    success_url = reverse_lazy('addblog')
    success_message = "Blog Added!!"
    context_object_name = 'students'

    def get_context_data(self, **kwargs):
        context = super(BlogCreateView, self).get_context_data(**kwargs)
        context['blogs'] = Blog.objects.all()
        return context

class BlogUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = "updateblog.html"
    success_message = "Blog Updated!!"
    success_url = '/addblog/'

class BlogDeteleView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Blog
    template_name = "blog_confirm_delete.html"
    success_url = '/addblog/'
    success_message = "Blog Deleted!!"

class BlogDetailsView(LoginRequiredMixin,DetailView):
    model = Blog
    template_name="demo.html"

class DisplayBlog(DetailView):
    model = Blog
    template_name="blog-detail.html"

