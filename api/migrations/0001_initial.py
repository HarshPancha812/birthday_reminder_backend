# Generated by Django 4.0.1 on 2022-02-08 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='birthday_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('user_id', models.IntegerField(blank=True, default='0', null=True)),
            ],
        ),
    ]
