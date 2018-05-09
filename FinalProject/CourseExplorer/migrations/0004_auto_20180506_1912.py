# Generated by Django 2.0.4 on 2018-05-06 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CourseExplorer', '0003_courseexplorerdata_ratemyprofessor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ratemyprofessor',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='ratemyprofessor',
            name='last_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]