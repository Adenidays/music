# Generated by Django 4.2.2 on 2023-07-01 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='phonk_singer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('age', models.PositiveIntegerField()),
                ('big_award', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('description', models.TextField(null=True)),
            ],
        ),
    ]