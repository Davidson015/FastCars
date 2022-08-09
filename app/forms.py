from django import forms
from app.models import *

# Booking form
class BookingForm(forms.ModelForm):
  class Meta:
    model = Booking
    fields = '__all__'

# Testimonial form
class TestimonialForm(forms.ModelForm):
  class Meta:
    model = Testimonial
    fields = '__all__'
    
# Contact form
class ContactForm(forms.ModelForm):
  class Meta:
    model = Contact
    fields = '__all__'
    # widgets = {
    #   'pick_up_date': forms.DateInput(attrs={'type': 'date'}),
    #   'drop_off_date': forms.DateInput(attrs={'type': 'date'}),
    #   'pick_up_time': forms.TimeInput(attrs={'type': 'time'}),
    #   'drop_off_time': forms.TimeInput(attrs={'type': 'time'}),
    # }