"""library_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.static import static

from LIBRARY.library_management_app import views
from LIBRARY.library_management_system import settings

urlpatterns = [
    path('', views.showHomePage),
   # path('books', views.showBooksPage),
    path('home', views.showHomePage),
    path('addBook', views.showAddBook),
    path('demo/', views.showDemoPage),
    path('admin/', admin.site.urls),
    path('add_book_save', views.addBook),
    path('books', views.viewBooks)
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
