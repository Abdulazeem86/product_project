# Generated by Django 5.0.3 on 2024-03-15 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0011_alter_productmodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='image',
            field=models.ImageField(blank=True, default='/productpics/default.jpg', null=True, upload_to='productpics'),
        ),
    ]
