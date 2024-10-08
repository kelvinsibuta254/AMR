# Generated by Django 5.1 on 2024-09-05 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeneBank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sample_id', models.CharField(max_length=10)),
                ('barcode_sequence', models.CharField(max_length=100)),
                ('primer_sequence', models.CharField(max_length=50)),
                ('gene', models.CharField(max_length=10)),
                ('region', models.CharField(max_length=50)),
                ('site', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=100)),
            ],
        ),
    ]
