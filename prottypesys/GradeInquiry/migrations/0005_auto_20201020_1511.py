# Generated by Django 3.1.2 on 2020-10-20 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GradeInquiry', '0004_auto_20201020_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginuser',
            name='username',
            field=models.CharField(default='', max_length=255, unique=True),
        ),
    ]
