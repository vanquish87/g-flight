# Generated by Django 4.0.5 on 2022-06-17 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bonuses', '0004_alter_magicbonus_directbonus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='discountbonus',
            old_name='admin_code',
            new_name='ref_code',
        ),
    ]
