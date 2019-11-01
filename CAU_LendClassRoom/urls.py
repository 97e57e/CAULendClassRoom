from django.contrib import admin
from django.urls import path, include

import accounts.urls
import main.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('', include('main.urls')),
]