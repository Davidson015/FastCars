from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from app.views import index, about, contact, faq, testimonials, gallery, reservation, car_details

urlpatterns = [
  path('', index, name='index'),
  path('about', about, name='about'),
  path('contact', contact, name='contact'),
  path('faq', faq, name='faq'),
  path('testimonials', testimonials, name='testimonials'),
  path('gallery', gallery, name='gallery'),
  path('reservation', reservation, name='reservation'),
  path('car_details', car_details, name='car_details'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)