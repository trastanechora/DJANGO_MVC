# Generated by Django 2.1.5 on 2019-02-11 07:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_mentee_nickname'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('Updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('Title', models.CharField(max_length=50)),
                ('Content', models.TextField(max_length=255)),
                ('Created_by', models.CharField(max_length=50)),
            ],
        ),
    ]