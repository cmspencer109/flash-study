# Generated by Django 3.2.9 on 2021-12-08 15:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('section_num', models.IntegerField()),
                ('semester', models.CharField(choices=[('spring', 'Spring'), ('summer', 'Summer'), ('fall', 'Fall'), ('winter', 'Winter')], max_length=6)),
                ('year', models.IntegerField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('major', models.CharField(max_length=50)),
                ('school_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='FlashcardDeck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('school_name', models.CharField(max_length=50)),
                ('public', models.BooleanField()),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('class_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flashcard_app.class')),
            ],
        ),
        migrations.CreateModel(
            name='Flashcard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('front', models.TextField()),
                ('back', models.TextField()),
                ('deck', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flashcard_app.flashcarddeck')),
            ],
        ),
        migrations.AddField(
            model_name='class',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flashcard_app.school'),
        ),
    ]
