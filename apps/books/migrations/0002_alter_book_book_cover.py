# Generated by Django 4.1.5 on 2023-02-04 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="book_cover",
            field=models.ImageField(upload_to="livros/", verbose_name="Capa"),
        ),
    ]
