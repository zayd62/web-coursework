# Generated by Django 2.2.6 on 2019-11-25 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20191125_0215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='picture',
            field=models.ImageField(upload_to='gallery'),
        ),
    ]