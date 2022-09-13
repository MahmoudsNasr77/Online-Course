# Generated by Django 4.1.1 on 2022-09-11 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Instructors', '0005_alter_instructor_categeory'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='github',
            field=models.URLField(default='https://github.com/'),
        ),
        migrations.AddField(
            model_name='instructor',
            name='linkdin',
            field=models.URLField(default='https://www.linkedin.com/'),
        ),
        migrations.AddField(
            model_name='instructor',
            name='twitter',
            field=models.URLField(default='https://www.facebook.com/'),
        ),
    ]