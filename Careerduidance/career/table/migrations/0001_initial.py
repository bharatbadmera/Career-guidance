# Generated by Django 2.1.3 on 2018-12-01 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=500)),
                ('body', models.TextField(max_length=800)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
