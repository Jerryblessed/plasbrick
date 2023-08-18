"""student_portal URL Configuration

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
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


from authy.views import UserProfile
from classroom.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('authy.urls')),
    path('info/', include('course.urls')),
    path('course/', include('classroom.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('direct/', include('direct.urls')),
    path('livestream/', include('livestream.urls')),
    path('<username>', UserProfile, name='profile'),
    path('class/', index, name='index'),
    path('',include('lms.urls')),
    path('', include('blog.urls')),
    path('api/v1/', include('blog.api.v1.routers.routers')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)