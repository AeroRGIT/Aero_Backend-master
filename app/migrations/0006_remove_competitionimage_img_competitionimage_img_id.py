# Generated by Django 4.0.2 on 2022-08-14 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_teammember_profileimg_teammember_img_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competitionimage',
            name='img',
        ),
        migrations.AddField(
            model_name='competitionimage',
            name='img_id',
            field=models.CharField(default='', max_length=100),
        ),
    ]
