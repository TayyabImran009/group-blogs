# Generated by Django 2.2.4 on 2022-06-08 00:26

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_groupjoined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcomment',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
