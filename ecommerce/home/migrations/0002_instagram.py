# Generated by Django 3.0.8 on 2020-07-10 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instagram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='instagram/image/')),
                ('text', models.CharField(blank=True, max_length=300, null=True)),
                ('active', models.BooleanField(default=True)),
                ('slug', models.SlugField()),
                ('featured', models.BooleanField(default=False)),
            ],
        ),
    ]
