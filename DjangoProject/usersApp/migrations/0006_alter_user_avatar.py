# Generated by Django 5.0.2 on 2024-03-26 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersApp', '0005_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='avatars/avatar.png', upload_to='avatars'),
        ),
    ]
