# Generated by Django 4.0.5 on 2022-06-16 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bonuses', '0001_initial'),
        ('accounts', '0003_referral'),
    ]

    operations = [
        migrations.AddField(
            model_name='referral',
            name='leadershipbonus',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bonuses.leadershipbonus'),
        ),
        migrations.AlterField(
            model_name='referral',
            name='code',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]