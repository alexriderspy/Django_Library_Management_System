# Generated by Django 3.2 on 2021-04-19 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_author_last_accessed'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='thesis',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
