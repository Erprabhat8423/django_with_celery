# Generated by Django 3.2.19 on 2023-06-11 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SpActivityLogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_name', models.CharField(blank=True, max_length=100, null=True)),
                ('app_name', models.CharField(blank=True, max_length=100, null=True)),
                ('developer', models.CharField(blank=True, max_length=100, null=True)),
                ('Price', models.FloatField(blank=True, max_length=100, null=True)),
                ('Rating', models.FloatField(blank=True, max_length=10, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('icon_url', models.URLField(blank=True, null=True)),
                ('cover_image', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
