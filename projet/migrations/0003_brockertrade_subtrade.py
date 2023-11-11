# Generated by Django 4.2.6 on 2023-11-09 23:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projet', '0002_category_rename_text_order_text_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='brockertrade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_brockertrade', models.TextField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='subtrade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_subtrade', models.TextField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now, null=True)),
            ],
        ),
    ]
