# Generated by Django 4.0.5 on 2022-06-30 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_under_empgroup_alias'),
    ]

    operations = [
        migrations.CreateModel(
            name='empgroup2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupname', models.CharField(max_length=50)),
                ('groupalias', models.CharField(max_length=50)),
                ('groupunder', models.CharField(max_length=50)),
            ],
        ),
    ]
