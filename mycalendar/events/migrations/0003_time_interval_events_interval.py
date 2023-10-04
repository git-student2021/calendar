# Generated by Django 4.2.5 on 2023-10-04 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_alter_events_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Time_interval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150, verbose_name='Интервал')),
            ],
            options={
                'verbose_name': 'Интервал',
                'verbose_name_plural': 'Интервалы',
                'ordering': ['title'],
            },
        ),
        migrations.AddField(
            model_name='events',
            name='interval',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='events.time_interval'),
        ),
    ]
