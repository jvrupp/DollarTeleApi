# Generated by Django 4.1.7 on 2023-02-14 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataBet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('digit', models.CharField(max_length=25)),
                ('color', models.CharField(max_length=25)),
                ('timestamp', models.DateTimeField()),
            ],
        ),
    ]