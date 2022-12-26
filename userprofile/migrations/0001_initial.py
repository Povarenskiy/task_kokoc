# Generated by Django 4.1.4 on 2022-12-23 10:35

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BackColors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', colorfield.fields.ColorField(default='#FF0000', image_field=None, max_length=18, samples=None, verbose_name='Цвет')),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BorderColors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', colorfield.fields.ColorField(default='#FF0000', image_field=None, max_length=18, samples=None, verbose_name='Цвет')),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reward', models.IntegerField(default=0, verbose_name='Награда пользователя')),
                ('background_color', models.ForeignKey(default='white', on_delete=django.db.models.deletion.SET_DEFAULT, to='userprofile.backcolors')),
                ('border_color', models.ForeignKey(default='white', on_delete=django.db.models.deletion.SET_DEFAULT, to='userprofile.bordercolors')),
            ],
        ),
    ]