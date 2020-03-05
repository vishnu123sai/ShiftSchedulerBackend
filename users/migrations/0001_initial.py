# Generated by Django 2.2.10 on 2020-03-04 11:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('designation', models.CharField(max_length=255)),
                ('project', models.CharField(choices=[('bench', 'Bench'), ('devops', 'Devops'), ('production', 'Production'), ('hr', 'HR'), ('lead', 'Leaders')], default='bench', max_length=255, null=True)),
                ('doj', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('gender', models.CharField(max_length=10)),
                ('permissions', models.CharField(default='V', max_length=1)),
                ('mobile_number', models.IntegerField(max_length=10, null=True)),
                ('total_exp', models.IntegerField(max_length=2, null=True)),
                ('project_exp', models.IntegerField(max_length=2, null=True)),
                ('img', models.ImageField(default=None, upload_to='empid')),
            ],
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=None)),
                ('shift', models.CharField(default='G', max_length=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
