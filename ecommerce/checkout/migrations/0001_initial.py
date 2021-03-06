# Generated by Django 3.0.8 on 2020-07-15 11:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Addres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(choices=[('S_A', 'SHIPPING_ADDRESS'), ('B_A', 'BILLING_ADDRESS')], max_length=1000)),
                ('first_name', models.CharField(max_length=1000)),
                ('last_name', models.CharField(max_length=1000)),
                ('phone_no', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('country', models.CharField(choices=[('IND', 'INDIA'), ('US', 'UNITED STATE'), ('UK', 'UNITED KIGNDOM')], max_length=1000)),
                ('street', models.CharField(max_length=10000)),
                ('town', models.CharField(max_length=1000)),
                ('state', models.CharField(max_length=100)),
                ('postal_code', models.IntegerField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
