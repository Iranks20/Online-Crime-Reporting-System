# Generated by Django 4.2.2 on 2023-10-10 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('police', '0004_rename_police_birth_date_police_birth_date'),
        ('citizen', '0001_initial'),
        ('comment', '0004_alter_comment_user1_alter_comment_user2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='police.police'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='citizen.citizen'),
        ),
    ]