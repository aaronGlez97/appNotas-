# Generated by Django 3.0.6 on 2020-07-13 16:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app1', '0002_auto_20200713_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notas',
            name='usuarionotas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
