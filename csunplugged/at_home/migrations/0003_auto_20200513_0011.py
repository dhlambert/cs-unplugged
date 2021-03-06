# Generated by Django 2.2.12 on 2020-05-13 00:11

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('at_home', '0002_auto_20200506_2051'),
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('languages', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), default=list, size=None)),
                ('order_number', models.PositiveSmallIntegerField(unique=True)),
                ('question', models.TextField(default='')),
                ('question_en', models.TextField(default='', null=True)),
                ('question_de', models.TextField(default='', null=True)),
                ('question_es', models.TextField(default='', null=True)),
                ('question_mi', models.TextField(default='', null=True)),
                ('question_zh_hans', models.TextField(default='', null=True)),
                ('question_xx_lr', models.TextField(default='', null=True)),
                ('question_yy_rl', models.TextField(default='', null=True)),
                ('answer', models.CharField(default='', max_length=200)),
                ('answer_en', models.CharField(default='', max_length=200, null=True)),
                ('answer_de', models.CharField(default='', max_length=200, null=True)),
                ('answer_es', models.CharField(default='', max_length=200, null=True)),
                ('answer_mi', models.CharField(default='', max_length=200, null=True)),
                ('answer_zh_hans', models.CharField(default='', max_length=200, null=True)),
                ('answer_xx_lr', models.CharField(default='', max_length=200, null=True)),
                ('answer_yy_rl', models.CharField(default='', max_length=200, null=True)),
            ],
            options={
                'ordering': ['order_number'],
            },
        ),
        migrations.AlterField(
            model_name='activity',
            name='languages',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), default=list, size=None),
        ),
        migrations.CreateModel(
            name='ChallengeAttempt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('language', models.CharField(max_length=25)),
                ('answer', models.CharField(default='', max_length=200)),
                ('correct', models.BooleanField()),
                ('challenge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='challenge_attempts', to='at_home.Challenge')),
            ],
        ),
        migrations.AddField(
            model_name='challenge',
            name='activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='challenges', to='at_home.Activity'),
        ),
    ]
