# Generated by Django 2.1.7 on 2019-04-02 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20190402_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='total',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=6),
            preserve_default=False,
        ),
    ]