# Generated by Django 2.2.3 on 2019-07-19 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userzone', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('aid', models.AutoField(primary_key=True, serialize=False)),
                ('answertext', models.TextField()),
                ('answeredby', models.CharField(max_length=50)),
                ('qid', models.IntegerField()),
                ('answereddate', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('qid', models.AutoField(primary_key=True, serialize=False)),
                ('questiontext', models.TextField()),
                ('askedby', models.CharField(max_length=50)),
                ('posteddate', models.CharField(max_length=30)),
            ],
        ),
    ]
