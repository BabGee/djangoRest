# Generated by Django 3.0.4 on 2020-03-28 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_auto_20200327_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='recipe_pics'),
        ),
    ]