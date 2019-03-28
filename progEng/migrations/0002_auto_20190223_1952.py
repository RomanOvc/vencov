# Generated by Django 2.1.5 on 2019-02-23 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('progEng', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='citizen',
            name='age',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='income',
            name='citizen_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='incomes', to='progEng.Citizen'),
        ),
    ]