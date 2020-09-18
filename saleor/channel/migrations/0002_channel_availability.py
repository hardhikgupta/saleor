# Generated by Django 3.1 on 2020-09-18 07:17

from django.db import migrations, models


def set_default_flag(apps, schema):
    Channel = apps.get_model("channel", "Channel")
    for channel in Channel.objects.iterator():
        if not channel.is_active:
            channel.is_active = True
        channel.save(update_fields=["is_active"])


class Migration(migrations.Migration):

    dependencies = [
        ("channel", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="channel",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.RunPython(set_default_flag, migrations.RunPython.noop),
    ]
