# Generated by Django 4.0.3 on 2022-08-18 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Posts', '0002_alter_post_caption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='caption',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]