# Generated by Django 2.2.5 on 2019-09-23 19:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='delivery_address',
            old_name='customerID',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='billing_address',
            name='customerID',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='customerID',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='last_name',
        ),
        migrations.AddField(
            model_name='billing_address',
            name='user',
            field=models.OneToOneField(default='7', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(default=7, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='title',
            field=models.CharField(choices=[('Prof', 'Prof'), ('Dr', 'Dr'), ('Lady', 'Lady'), ('Mrs', 'Mrs'), ('Ms', 'Ms'), ('Miss', 'Miss'), ('Mr', 'Mr'), ('Sir', 'Sir')], default='Mrs', max_length=4),
        ),
    ]
