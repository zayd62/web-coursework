# Generated by Django 2.2.6 on 2019-11-25 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_remove_auction_highestbid'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='highestBid',
            field=models.ForeignKey(default='2', on_delete=django.db.models.deletion.CASCADE, to='website.Bid'),
        ),
    ]