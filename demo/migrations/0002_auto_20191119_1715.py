# Generated by Django 2.2.7 on 2019-11-19 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tech',
            name='short_name',
        ),
        migrations.AlterField(
            model_name='tech',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]