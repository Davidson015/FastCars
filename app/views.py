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

# Reviews view
def reviews(request):
  template_name = 'review.html'

  context = {
    'current': 'reviews'
  }

  return render(request, template_name, context)