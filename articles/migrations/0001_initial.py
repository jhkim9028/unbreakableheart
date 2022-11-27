# Generated by Django 3.2.13 on 2022-11-27 12:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('picture', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='images/')),
                ('disclosure', models.BooleanField(default=True)),
                ('feelings', models.CharField(choices=[('1', '👿'), ('2', '😞'), ('3', '😊')], max_length=2)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
