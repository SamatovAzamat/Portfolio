# Generated by Django 4.0.1 on 2022-02-01 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('subject', models.TextField(verbose_name='subject')),
                ('message', models.TextField(verbose_name='message')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at ')),
            ],
            options={
                'verbose_name': 'contact',
                'verbose_name_plural': 'contacts',
            },
        ),
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='post/', verbose_name='image')),
                ('username', models.CharField(max_length=50, verbose_name='username')),
                ('header', models.CharField(max_length=100, verbose_name='header')),
                ('body', models.CharField(max_length=200, verbose_name='body')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
            ],
            options={
                'verbose_name': 'post',
                'verbose_name_plural': 'posts',
            },
        ),
    ]
