# Generated by Django 3.1.3 on 2020-11-12 02:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('learning_logs', '0002_auto_20201107_0643'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
