# Generated by Django 4.1.3 on 2022-11-14 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_rename_subscribers_subscriber'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscriber',
            options={'verbose_name': 'list_of_User', 'verbose_name_plural': 'List_of_Users'},
        ),
    ]