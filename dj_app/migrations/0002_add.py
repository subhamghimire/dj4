# Generated by Django 2.2 on 2019-05-27 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dj_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=100)),
                ('conent', models.TextField()),
            ],
        ),
    ]
