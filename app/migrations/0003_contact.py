# Generated by Django 4.0.6 on 2022-08-09 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_testimonial_alter_vehicle_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(help_text='example@email.com', max_length=100)),
                ('phone_number', models.CharField(help_text='+234 012 345 6789', max_length=100)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
    ]