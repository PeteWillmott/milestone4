# Generated by Django 2.2.5 on 2019-09-29 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalogue',
            name='finish',
            field=models.DateTimeField(null=True, verbose_name='Auction finishes'),
        ),
        migrations.AddField(
            model_name='catalogue',
            name='increment',
            field=models.DecimalField(decimal_places=2, default=10, max_digits=10),
        ),
        migrations.AddField(
            model_name='catalogue',
            name='reserve',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='catalogue',
            name='start',
            field=models.DateTimeField(null=True, verbose_name='Auction starts'),
        ),
        migrations.AlterField(
            model_name='catalogue',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]
