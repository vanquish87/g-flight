# Generated by Django 4.0.5 on 2022-06-17 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bonuses', '0003_alter_discountbonus_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='magicbonus',
            name='directbonus',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='bonuses.directbonus'),
        ),
    ]
