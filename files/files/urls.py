"""
URL configuration for files project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from docs import views as docs_views
from register import views as reg_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', include('register.urls')),
    # path('docs/', include('docs.urls')),
    path('list/',docs_views.upload_file,name='list'),
    path('login/',reg_views.register_index, name='reg_index'),
    path('contact/',docs_views.index,)

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
