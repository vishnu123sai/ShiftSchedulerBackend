# Generated by Django 2.2.10 on 2020-03-12 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200312_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='full_name',
            field=models.CharField(blank=True, default='None', max_length=255, null=True),
        ),
    ]
