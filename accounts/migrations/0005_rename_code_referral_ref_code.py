# Generated by Django 4.0.5 on 2022-06-17 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_referral_leadershipbonus_alter_referral_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='referral',
            old_name='code',
            new_name='ref_code',
        ),
    ]
