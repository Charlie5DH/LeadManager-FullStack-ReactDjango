from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # from the root path, include the leads url file, as part of
    # the urls
    path('', include('leads.urls'))
]
