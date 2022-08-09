from multiprocessing import context
from django.shortcuts import render

# Create your views here.

# Index view
def index(request):
  template_name = 'index.html'

  context = {
    'current': 'index'
  }

  return render(request, template_name, context)

# About view
def about(request):
  template_name = 'about.html'

  context = {
    'current': 'about'
  }

  return render(request, template_name, context)

# Contact view
def contact(request):
  template_name = 'contact.html'

  context = {
    'current': 'contact'
  }

  return render(request, template_name, context)

# Faq view
def faq(request):
  template_name = 'faq.html'

  context = {
    'current': 'faq'
  }

  return render(request, template_name, context)

# Testimonials view
def testimonials(request):
  template_name = 'reviews.html'

  context = {
    'current': 'testimonials'
  }

  return render(request, template_name, context)

# Gallery view
def gallery(request):
  template_name = 'gallery.html'

  context = {
    'current': 'gallery'
  }

  return render(request, template_name, context)

# Reservation view
def reservation(request):
  template_name = 'reservation.html'

  context = {
    'current': 'reservation'
  }

  return render(request, template_name, context)

# Car Detail view
def car_details(request):
  template_name = 'car_details.html'

  context = {
    'current': 'car_details'
  }

  return render(request, template_name, context)

