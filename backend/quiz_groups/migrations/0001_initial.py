# Generated by Django 3.0.3 on 2020-03-25 03:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('files', '0002_files_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tags', '0002_tags_user'),
        ('quizzes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_public', models.BooleanField(default=True)),
                ('file', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='files.Files')),
                ('quizzes', models.ManyToManyField(blank=True, to='quizzes.Quizzes')),
                ('tags', models.ManyToManyField(blank=True, to='tags.Tags')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Quiz Group',
                'verbose_name_plural': 'Quiz Groups',
            },
        ),
    ]
