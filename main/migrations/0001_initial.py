# Generated by Django 5.0 on 2023-12-18 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_url', models.CharField(max_length=10000)),
                ('shortened_url', models.CharField(max_length=100)),
                ('uuid', models.CharField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
