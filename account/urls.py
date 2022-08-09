from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from account.views import account

urlpatterns = [
  path('account', account, name='account'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
