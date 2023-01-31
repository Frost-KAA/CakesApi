# Generated by Django 4.1.4 on 2023-01-31 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cake',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=90)),
                ('price', models.DecimalField(decimal_places=0, max_digits=4)),
                ('desc', models.CharField(max_length=255)),
                ('upload', models.ImageField(upload_to='uploads/')),
            ],
        ),
    ]
