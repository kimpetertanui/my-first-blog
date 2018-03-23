from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from blog.views import post_list
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
]