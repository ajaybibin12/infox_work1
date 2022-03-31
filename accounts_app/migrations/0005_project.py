# Generated by Django 4.0.2 on 2022-03-24 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_app', '0004_rename_clogo_company_companylogo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_title', models.CharField(max_length=100, primary_key='true', serialize=False, unique='true')),
                ('project_value', models.CharField(max_length=50)),
                ('contract_length', models.CharField(max_length=50)),
                ('client_email', models.EmailField(max_length=254)),
                ('client_phoneno', models.CharField(max_length=50)),
            ],
        ),
    ]
