# Generated by Django 5.0.5 on 2024-05-09 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_view_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('studentNumber', models.IntegerField(default=24, verbose_name='학번')),
                ('contentn', models.TextField(verbose_name='자기소개')),
                ('image', models.ImageField(upload_to='', verbose_name='이미지')),
                ('created_at', models.DateTimeField(verbose_name='작성일')),
            ],
        ),
    ]
