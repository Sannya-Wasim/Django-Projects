# Generated by Django 4.2.4 on 2023-08-28 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=255)),
                ('employee_des', models.CharField(max_length=255)),
                ('employee_contact', models.IntegerField(default=99999999999)),
            ],
        ),
    ]
