# Generated by Django 2.2.1 on 2019-05-13 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='addcategory',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='addpost',
            name='posted_by',
            field=models.CharField(default='sss', max_length=120),
        ),
        migrations.AddField(
            model_name='addpost',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]