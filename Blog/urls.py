"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from posts.views import main_view,  post_detail_view, hashtags_view, post_create_view, PostsCBV
from products.views import product_create_view, ProductsCBV, CategoriesCBV, ProductDetailView
from Blog import settings
from django.conf.urls.static import static
from users.views import login_view, logout_view, register_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view),
    path('posts/', PostsCBV.as_view()),
    path('products/', ProductsCBV.as_view()),
    path('posts/<int:id>/', post_detail_view),
    path('posts/create/', post_create_view),
    path('hashtags/', hashtags_view),
    path('products/<int:id>/', ProductDetailView.as_view()),
    path('products/create/', product_create_view),
    path('categories/', CategoriesCBV.as_view()),

    path('users/login/', login_view),
    path('users/register/', register_view),
    path('users/logout/', logout_view)

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
