# Generated by Django 4.2 on 2023-05-16 09:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('plusdefapp', '0002_rename_chatgptcb_chatgptcbot'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatGptBot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messageInput', models.TextField()),
                ('bot_response', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
