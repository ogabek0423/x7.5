# Generated by Django 5.0.6 on 2024-05-12 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_comments_users_comme_id_c30fad_idx_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default='2023-01-10'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='problems',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2023-9-11'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='creation_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]