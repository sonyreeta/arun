# Generated by Django 5.1.1 on 2024-11-28 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('Type_of_Project', models.TextField(blank=True)),
                ('Project_Description', models.TextField(blank=True)),
                ('Project_Requirements', models.TextField(blank=True)),
                ('Address', models.CharField(blank=True, max_length=100, null=True)),
                ('Phone_Number', models.IntegerField(blank=True)),
                ('Email', models.EmailField(blank=True, max_length=254)),
                ('message', models.TextField(blank=True)),
            ],
        ),
    ]
