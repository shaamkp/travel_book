# Generated by Django 4.2.2 on 2024-03-11 09:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destinations',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_deleted', models.BooleanField(blank=True, default=False, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('destination_id', models.CharField(blank=True, max_length=128, null=True)),
                ('destination_name', models.CharField(blank=True, max_length=128, null=True)),
                ('country', models.CharField(blank=True, max_length=128, null=True)),
                ('popular_season', models.CharField(blank=True, choices=[('winter', 'Winter'), ('summer', 'Summer'), ('autumn', 'Autumn'), ('spring', 'Spring')], max_length=128, null=True)),
            ],
            options={
                'verbose_name': 'Destination',
                'verbose_name_plural': 'Destinations',
                'db_table': 'destinations_destination',
                'ordering': ('-created_at',),
            },
        ),
    ]
