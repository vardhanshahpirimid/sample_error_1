# Generated by Django 2.2.22 on 2021-05-21 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='title',
            field=models.CharField(default='vardhan', max_length=50),
            preserve_default=False,
        ),
    ]