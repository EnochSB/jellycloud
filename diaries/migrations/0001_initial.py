# Generated by Django 3.2.18 on 2023-06-14 07:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Content')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('thumbnail', models.CharField(blank=True, max_length=500)),
                ('hit', models.ManyToManyField(blank=True, related_name='diary_views', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DiaryShare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('diary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diaries.diary')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.group')),
            ],
        ),
        migrations.CreateModel(
            name='DiaryComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('like_users', models.ManyToManyField(related_name='like_diarycomments', to=settings.AUTH_USER_MODEL)),
                ('share', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diaries.diaryshare')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.AddField(
            model_name='diary',
            name='share',
            field=models.ManyToManyField(related_name='group_diaries', through='diaries.DiaryShare', to='groups.Group', verbose_name='shared diary to group'),
        ),
        migrations.AddField(
            model_name='diary',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='DiaryEmote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emotion', models.PositiveIntegerField()),
                ('share', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diaries.diaryshare')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emotions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'share')},
            },
        ),
    ]