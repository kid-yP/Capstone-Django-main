# Generated by Django 4.2.11 on 2024-03-13 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookApp', '0007_book_borrowers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover_image',
            field=models.ImageField(default='defaults/no-cover.jpeg', upload_to='Book-Covers/'),
        ),
    ]
