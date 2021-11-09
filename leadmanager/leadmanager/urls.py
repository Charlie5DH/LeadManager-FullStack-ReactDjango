#from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # from the root path, include the leads url file, as part of
    # the urls
    path('', include('frontend.urls')),
    path('', include('leads.urls'))
]
