# Generated by Django 2.1.7 on 2019-04-02 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20190402_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='subtotal',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
