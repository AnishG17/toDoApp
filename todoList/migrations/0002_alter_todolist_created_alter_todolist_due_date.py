# Generated by Django 4.0.5 on 2023-06-22 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoList', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='created',
            field=models.DateField(default='2023-06-22'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='due_date',
            field=models.DateField(default='2023-06-22'),
        ),
    ]
