# Generated by Django 5.1.3 on 2025-04-03 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mentorados", "0002_disponibilidadedehorarios"),
    ]

    operations = [
        migrations.AddField(
            model_name="mentorados",
            name="token",
            field=models.CharField(default=1, max_length=16),
            preserve_default=False,
        ),
    ]
