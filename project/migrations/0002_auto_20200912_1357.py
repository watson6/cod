# Generated by Django 2.2.14 on 2020-09-12 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.CharField(default='4efa211312614110a054f9d88c4e3274', max_length=32, primary_key=True, serialize=False, unique=True, verbose_name='id'),
        ),
    ]
