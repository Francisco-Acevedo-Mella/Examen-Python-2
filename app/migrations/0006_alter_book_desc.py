# Generated by Django 4.0.2 on 2022-03-06 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
    ]
