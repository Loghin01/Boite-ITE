# Generated by Django 4.0.2 on 2022-02-28 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_alter_data_box'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='box',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.box'),
        ),
    ]
