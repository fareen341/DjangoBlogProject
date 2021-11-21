from django.urls import path, include
from BlogApp import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.BaseView, {'template_name':'index.html'}, name='home'),
    path('about/',views.About, name="about"),
    path('author/',views.Author, name="author"),
    path('addblog/',views.BlogCreateView.as_view(), name="addblog"),
    path('updateblog/<int:pk>',views.BlogUpdateView.as_view()),
    path('deleteblog/<int:pk>', views.BlogDeteleView.as_view(), name="deleteblog"),
    path('detail/<int:pk>', views.BlogDetailsView.as_view(), name="detail"),
    path('blogdetail/<slug>', views.DisplayBlog.as_view(), name="blogdetail"),
    # path('login/', include('django.contrib.auth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', views.Loginuser, name="login"),
    path('accounts/login/', views.Loginuser, name="login"),    


    # path('addblog/',views.BlogDetailsView.as_view(), name="addblog"),
    # path('addshowblog/',views.AddShowBlog, name="addshowblog")

]

