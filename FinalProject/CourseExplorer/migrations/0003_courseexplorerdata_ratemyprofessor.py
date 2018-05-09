# Generated by Django 2.0.4 on 2018-05-06 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CourseExplorer', '0002_kooferdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseExplorerData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('number', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='RateMyProfessor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avg_rating', models.FloatField(default=0.0)),
                ('total_ratings', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=100)),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CourseExplorer.CourseExplorerData')),
            ],
        ),
    ]
