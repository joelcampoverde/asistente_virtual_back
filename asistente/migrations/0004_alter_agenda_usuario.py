# Generated by Django 4.2.16 on 2024-11-21 04:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('asistente', '0003_alter_agenda_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='agenda', to=settings.AUTH_USER_MODEL),
        ),
    ]
