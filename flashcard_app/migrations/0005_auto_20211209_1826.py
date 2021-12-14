# Generated by Django 3.2.9 on 2021-12-09 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcard_app', '0004_auto_20211208_1634'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='school',
        ),
        migrations.RemoveField(
            model_name='flashcarddeck',
            name='public',
        ),
        migrations.RemoveField(
            model_name='flashcarddeck',
            name='school',
        ),
        migrations.AlterField(
            model_name='course',
            name='section_num',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='semester',
            field=models.CharField(blank=True, choices=[('Spring', 'Spring'), ('Summer', 'Summer'), ('Fall', 'Fall'), ('Winter', 'Winter')], max_length=6),
        ),
        migrations.AlterField(
            model_name='course',
            name='year',
            field=models.IntegerField(blank=True),
        ),
        migrations.DeleteModel(
            name='School',
        ),
    ]