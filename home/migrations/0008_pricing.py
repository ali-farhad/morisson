# Generated by Django 3.1 on 2020-08-12 15:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20200812_1330'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateField(default=django.utils.timezone.now)),
                ('fname', models.CharField(max_length=64)),
                ('lname', models.CharField(max_length=64)),
                ('cname', models.CharField(max_length=64)),
                ('phone', models.CharField(max_length=64)),
                ('email', models.CharField(max_length=64)),
                ('checks', models.CharField(max_length=30)),
                ('message', models.CharField(max_length=1000)),
            ],
        ),
    ]