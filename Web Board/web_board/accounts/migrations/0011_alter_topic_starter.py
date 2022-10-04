# Generated by Django 4.1.1 on 2022-10-03 11:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0010_board_board_starter_alter_topic_starter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='starter',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
