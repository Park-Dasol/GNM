# Generated by Django 3.1.7 on 2021-04-05 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guestbook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_nickname', models.CharField(max_length=15)),
                ('guestbook_comment', models.CharField(max_length=144)),
                ('guestbook_password', models.CharField(max_length=20)),
                ('guestbook_image', models.CharField(blank=True, max_length=100, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
