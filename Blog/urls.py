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
from posts.views import main_view, posts_view,  post_detail_view, hashtags_view, post_create_view
from products.views import products_view, product_detail_view, categories_view, product_create_view
from Blog import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view),
    path('posts/', posts_view),
    path('products/', products_view),
    path('posts/<int:id>/', post_detail_view),
    path('posts/create/', post_create_view),
    path('hashtags/', hashtags_view),
    path('products/<int:id>/', product_detail_view),
    path('products/create/', product_create_view),
    path('categories/', categories_view)

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
