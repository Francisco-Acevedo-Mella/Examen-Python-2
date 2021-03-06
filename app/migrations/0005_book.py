# Generated by Django 4.0.2 on 2022-03-02 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_user_email_user_nacimiento_delete_deseos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('desc', models.TextField()),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_uploaded', to='app.user')),
                ('user_who_like', models.ManyToManyField(related_name='liked_books', to='app.User')),
            ],
        ),
    ]
