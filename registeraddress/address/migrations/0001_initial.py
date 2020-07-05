# Generated by Django 3.0.8 on 2020-07-04 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(max_length=8)),
                ('address', models.CharField(max_length=30)),
                ('number', models.CharField(max_length=6)),
                ('complement', models.CharField(blank=True, max_length=30, null=True)),
                ('neighborhood', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('uf', models.CharField(max_length=2)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]