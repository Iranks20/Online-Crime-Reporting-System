# Generated by Django 4.2.2 on 2023-08-11 07:47

from django.db import migrations, models
import django.db.models.deletion
import police.models


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0004_alter_case_approved_alter_case_case_categories_and_more'),
        ('police', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='criminal',
            name='ward',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='police.ward'),
        ),
        migrations.AlterField(
            model_name='police',
            name='ward',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='police.ward'),
        ),
        migrations.CreateModel(
            name='Evidence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evidence_type', models.CharField(max_length=255)),
                ('details', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to=police.models.image_upload_location)),
                ('video', models.FileField(blank=True, null=True, upload_to=police.models.video_upload_location)),
                ('document', models.FileField(blank=True, null=True, upload_to=police.models.doc_upload_location)),
                ('audio', models.FileField(blank=True, null=True, upload_to=police.models.audio_upload_location)),
                ('case', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='police_evidence', to='case.case')),
            ],
        ),
    ]
