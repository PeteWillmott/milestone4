# Generated by Django 2.2.5 on 2019-09-29 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0004_auto_20190929_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='catalogue.Catalogue'),
        ),
    ]
