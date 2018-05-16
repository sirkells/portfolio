# Generated by Django 2.0.2 on 2018-05-15 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('date', models.DateTimeField()),
                ('image', models.ImageField(upload_to='images')),
                ('body_text', models.CharField(max_length=2000)),
            ],
        ),
    ]