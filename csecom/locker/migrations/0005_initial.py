# Generated by Django 4.0 on 2023-07-13 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0011_rename_locker_used_user_locker_number'),
        ('locker', '0004_delete_locker'),
    ]

    operations = [
        migrations.CreateModel(
            name='Locker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locker_id', models.IntegerField(null=0)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.user')),
            ],
        ),
    ]
