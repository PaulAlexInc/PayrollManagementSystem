# Generated by Django 3.1.3 on 2021-01-09 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0008_auto_20210108_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salary_mgmt',
            name='Desc',
            field=models.CharField(default='None', max_length=200),
        ),
    ]