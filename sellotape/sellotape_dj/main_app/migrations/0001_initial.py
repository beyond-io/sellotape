# Generated by Django 3.1.1 on 2020-09-26 21:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(upload_to='')),
                ('country', models.CharField(default='Israel', max_length=100)),
                ('youtube_link', models.URLField(blank=True)),
                ('twitch_link', models.URLField(blank=True)),
                ('city', models.IntegerField(choices=[(1, 'Tel Aviv'), (2, 'HaMerkaz'), (3, 'HaDarom'), (4, 'HaTzafon')], default=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(max_length=500)),
                ('description', models.TextField(blank=True, max_length=50, null=True)),
                ('airs_on', models.DateTimeField()),
                ('ends_on', models.DateTimeField(blank=True, null=True)),
                ('added_on', models.DateTimeField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.profile')),
            ],
            options={
                'db_table': 'streams',
                'ordering': ['airs_on', '-added_on', 'author'],
            },
        ),
        migrations.CreateModel(
            name='UserFollowers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follow_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow_from', to='main_app.profile')),
                ('follow_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow_to', to='main_app.profile')),
            ],
            options={
                'unique_together': {('follow_from', 'follow_to')},
            },
        ),
    ]