# Generated by Django 4.1.4 on 2022-12-23 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='background_color',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='userprofile.backcolors'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='border_color',
            field=models.ForeignKey(default='#FF0000', null=True, on_delete=django.db.models.deletion.SET_NULL, to='userprofile.bordercolors'),
        ),
    ]
