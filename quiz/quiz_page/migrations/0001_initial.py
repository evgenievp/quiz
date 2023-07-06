# Generated by Django 4.1.7 on 2023-07-06 09:44

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(max_length=300, validators=[django.core.validators.MinLengthValidator(10)])),
                ('option_1', models.CharField(default='A', max_length=100)),
                ('option_2', models.CharField(default='B', max_length=100)),
                ('option_3', models.CharField(default='C', max_length=100)),
                ('option_4', models.CharField(default='D', max_length=100)),
                ('correct_option', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default=models.CharField(default='D', max_length=100), max_length=200)),
                ('topic', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='quiz_page.category')),
            ],
        ),
    ]
