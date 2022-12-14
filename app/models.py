from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
# Vehicle Brands Model
class Brand(models.Model):

  name = models.CharField(max_length=100)
  slug = models.SlugField(max_length=500, unique=True, blank=True)

  class Meta:
    verbose_name = ("Brand")
    verbose_name_plural = ("Brands")

  def __str__(self):
    return self.name

  def save(self, *args, **kwargs):
    slug = self.name
    self.slug = slugify(slug, allow_unicode=True)
    super().save(*args, **kwargs)

  def get_absolute_url(self):
    return reverse("Brand_detail", kwargs={"pk": self.pk})

# Vehicle Model
class Vehicle(models.Model):

  model = models.CharField(max_length=250)
  make = models.ForeignKey(Brand, on_delete=models.CASCADE)
  image = models.ImageField(upload_to='images/vehicles/', blank=True)
  description = models.TextField(blank=True)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  year = models.IntegerField()
  slug = models.SlugField(max_length=500, unique=True, blank=True)

  class Meta:
    verbose_name = ("Vehicle")
    verbose_name_plural = ("Vehicles")

  def __str__(self):
    return f'{self.make.name.upper()} {self.model.capitalize()}'

  def save(self, *args, **kwargs):
    slug = self.name
    self.slug = slugify(slug, allow_unicode=True)
    super().save(*args, **kwargs)

  def get_absolute_url(self):
    return reverse("Vehicle_detail", kwargs={"pk": self.pk})

# Booking Model
class Booking(models.Model):
  
  vehicles = ()

  # getting the vehicles from the vehicle model to store in the vehicles tuple
  def get_vehicles(self):
    vehicles = Vehicle.objects.all()
    for v in vehicles:
      self.vehicles.__add__((f'{v.make.name.upper()} {v.model.capitalize()}', f'{v.make.name.upper()} {v.model.capitalize()}'))

  pick_up_location = models.CharField(max_length=500)
  pick_up_date = models.DateField(blank=False)
  pick_up_time = models.TimeField(blank=False)
  drop_off_location = models.CharField(max_length=500)
  drop_off_date = models.DateField(blank=False)
  drop_off_time = models.TimeField(blank=False)
  get_help_location = models.BooleanField(default=False)
  get_chaffeur_driven = models.BooleanField(default=False)
  vehicle = models.CharField(choices=vehicles, max_length=250)

  class Meta:
    verbose_name = ("Booking")
    verbose_name_plural = ("Bookings")

  def __str__(self):
    return f'To Pick up at: {self.pick_up_location.upper()} \nTo Drop off at: {self.drop_off_location}'
  
  def save(self, *args, **kwargs):
    self.get_vehicles()
    super().save(*args, **kwargs)

  def get_absolute_url(self):
    return reverse("Booking_detail", kwargs={"pk": self.pk})

# Testimonial Model
class Testimonial(models.Model):

  review = models.TextField(blank=False)
  client_image = models.ImageField(upload_to='images/testimonials/', blank=True)
  client_name = models.CharField(max_length=100)
  rating = models.IntegerField(blank=False)

  class Meta:
    verbose_name = ("Testimonial")
    verbose_name_plural = ("Testimonials")

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse("Testimonial_detail", kwargs={"pk": self.pk})

# Contact Model
class Contact(models.Model):

  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  email = models.EmailField(max_length=100, help_text='example@email.com')
  phone_number = models.CharField(max_length=100, help_text='+234 012 345 6789')
  message = models.TextField(blank=False)

  class Meta:
    verbose_name = ("Contact")
    verbose_name_plural = ("Contacts")

  def __str__(self):
    return f'{self.first_name} ================= {self.email}'

  def get_absolute_url(self):
    return reverse("Contact_detail", kwargs={"pk": self.pk})
