# Generated by Django 4.0 on 2023-01-14 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0003_alter_user_division'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='division',
            field=models.CharField(max_length=10),
        ),
    ]
