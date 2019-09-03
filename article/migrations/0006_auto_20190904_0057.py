# Generated by Django 2.2.4 on 2019-09-03 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_comment_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='approved_comment',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(max_length=600),
        ),
    ]
