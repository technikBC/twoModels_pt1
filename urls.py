From django.conf.urls import url, include
From django.views.generic import ListView, DetailView
From reviews.models import ModelOne, ModelTwo
From reviews import views

urlpatterns =
[url(r'^$', views.review_page.as_view(), name='review_page'),
]


###
#In your main urls.py file (ie, the one above is your app urls.py file)
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^reviews/', include('reviews.urls')),
]
