# Generated by Django 4.1.7 on 2023-03-10 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frm', models.CharField(max_length=3)),
                ('to', models.CharField(max_length=3)),
                ('datetime', models.DateTimeField()),
            ],
        ),
    ]
