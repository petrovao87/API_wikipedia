# Generated by Django 2.2.5 on 2019-09-09 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0004_auto_20190908_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='content',
            field=models.CharField(max_length=100000, null=True),
        ),
    ]
