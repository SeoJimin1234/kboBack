# Generated by Django 4.2.13 on 2024-06-14 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
        ('users', '0007_alter_user_my_team_alter_user_nickname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='my_team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='games.team'),
        ),
    ]
