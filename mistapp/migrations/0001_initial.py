# Generated by Django 4.0.2 on 2022-02-22 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sorev',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=150, verbose_name='Названия')),
                ('descriptions', models.TextField(default='', max_length=3000, verbose_name='Описание')),
                ('Members', models.CharField(default='', max_length=150, verbose_name='Участники')),
                ('Result', models.CharField(default='', max_length=150, verbose_name='Результаты')),
            ],
        ),
    ]
