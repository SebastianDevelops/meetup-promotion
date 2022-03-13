# Generated by Django 4.0.3 on 2022-03-13 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letsmeet', '0003_location_meetups_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='meetups',
            name='participants',
            field=models.ManyToManyField(blank=True, to='letsmeet.participant'),
        ),
    ]