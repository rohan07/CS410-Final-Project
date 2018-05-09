# Generated by Django 2.0.4 on 2018-05-08 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CourseExplorer', '0005_reviews'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='polarity',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='reviews',
            name='sentiment',
            field=models.CharField(default='Neutral', max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reviews',
            name='subjectivity',
            field=models.FloatField(default=0.0),
        ),
    ]
