# Generated by Django 5.0 on 2024-01-01 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_social_github_profile_social_facebook_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='fvrt_activities',
            new_name='activities',
        ),
    ]