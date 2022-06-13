from django.contrib import admin
from django.urls import path, include

from blog.views import splash

urlpatterns = [
    path('', splash, name='splash'),
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls)
]
