from django.shortcuts import render

# Create your views here.

# Account view
def account(request):
  template_name = 'account.html'

  context = {
    'current': 'account'
  }

  return render(request, template_name, context)