# Generated by Django 2.0.7 on 2021-05-02 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valuea', models.CharField(max_length=10)),
                ('valueb', models.CharField(max_length=10)),
                ('result', models.CharField(max_length=10)),
            ],
        ),
    ]
