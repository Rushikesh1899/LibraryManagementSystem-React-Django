# Generated by Django 4.1.1 on 2022-09-14 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DetailsBook',
            fields=[
                ('BookId', models.AutoField(primary_key=True, serialize=False)),
                ('bookName', models.CharField(max_length=50)),
                ('authorName', models.CharField(max_length=50)),
                ('language', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=50)),
            ],
        ),
    ]
