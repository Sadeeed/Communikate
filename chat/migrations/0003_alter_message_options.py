# Generated by Django 3.2.6 on 2021-08-21 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_alter_chatroom_usercount'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ('msgTimestamp',)},
        ),
    ]
