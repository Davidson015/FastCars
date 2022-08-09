from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from app.views import account

urlpatterns = [
  path('account', account, name='account'),
]
