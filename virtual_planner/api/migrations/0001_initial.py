# Generated by Django 3.2 on 2021-04-25 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1000)),
                ('due_date', models.DateField()),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
