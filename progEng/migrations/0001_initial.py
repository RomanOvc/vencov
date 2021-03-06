# Generated by Django 2.1.7 on 2019-02-19 23:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Citizen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.TextField(max_length=100)),
                ('city', models.TextField(max_length=100)),
                ('profession', models.TextField(max_length=100)),

            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('income', models.IntegerField()),
                ('citizen_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Incomes', to='progEng.Citizen')),
            ],
        ),
    ]
