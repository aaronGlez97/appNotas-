# Generated by Django 3.0.6 on 2020-07-18 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20200713_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notas',
            name='nota',
            field=models.TextField(),
        ),
    ]
