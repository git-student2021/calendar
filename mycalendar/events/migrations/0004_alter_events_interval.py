# Generated by Django 4.2.5 on 2023-10-04 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_time_interval_events_interval'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='interval',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='events.time_interval', verbose_name='Интервал'),
        ),
    ]
