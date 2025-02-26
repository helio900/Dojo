# Generated by Django 5.1.1 on 2025-02-15 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dojo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('description', models.TextField()),
                ('history', models.TextField()),
                ('sensei', models.CharField(max_length=100)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='dojo_photos/')),
            ],
        ),
    ]
