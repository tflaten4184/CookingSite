# Generated by Django 4.2 on 2023-05-17 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to.', related_name='%(app_label)s_%(class)s_groups', related_query_name='%(app_label)s_%(class)s', to='auth.group', verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='%(app_label)s_%(class)s_user_permissions', related_query_name='%(app_label)s_%(class)s', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
