# Generated by Django 5.0.4 on 2024-04-20 02:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0003_alter_review_author"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="author",
            field=models.CharField(max_length=20),
        ),
    ]