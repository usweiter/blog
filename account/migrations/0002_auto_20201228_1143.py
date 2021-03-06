# Generated by Django 3.1.4 on 2020-12-28 08:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='modelprofile',
            old_name='photo',
            new_name='avatar',
        ),
        migrations.AddField(
            model_name='modelprofile',
            name='about',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='modelprofile',
            name='description',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='modelprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
