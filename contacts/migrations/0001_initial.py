# Generated by Django 3.1.5 on 2021-01-19 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('baseentity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='contacts.baseentity')),
                ('title', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=80)),
                ('is_active', models.BooleanField(default=True)),
            ],
            bases=('contacts.baseentity',),
        ),
    ]
