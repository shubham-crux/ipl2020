# Generated by Django 3.1 on 2020-09-08 12:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('score_app', '0003_auto_20200907_1209'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wins',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pointswon', models.IntegerField()),
                ('windate', models.DateField(default=datetime.date.today)),
                ('matchdetail', models.ManyToManyField(to='score_app.Matches')),
                ('playerdetail', models.ManyToManyField(to='score_app.Players')),
                ('rankdetail', models.ManyToManyField(to='score_app.Rankings')),
            ],
        ),
    ]
