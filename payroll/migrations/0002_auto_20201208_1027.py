# Generated by Django 3.1.3 on 2020-12-08 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee_details',
            name='Email_id',
        ),
        migrations.RemoveField(
            model_name='salary_mgmt',
            name='Ded_amt',
        ),
    ]
