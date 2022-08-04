from django.shortcuts import render

# Create your views here.

# Index view
def index(request):
  template_name = 'index.html'

  return render(request, template_name)

# About view
def about(request):
  template_name = 'about.html'

  return render(request, template_name)

