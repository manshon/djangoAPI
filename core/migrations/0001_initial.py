# Generated by Django 2.0.4 on 2018-05-16 08:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='氏名')),
                ('email', models.EmailField(max_length=254, verbose_name='メールアドレス')),
                ('age', models.IntegerField(verbose_name='年齢')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, verbose_name='登録日時')),
            ],
            options={
                'db_table': 'customer',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='CustomerLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(verbose_name='支払い金額')),
                ('note', models.TextField(blank=True, null=True, verbose_name='メモ')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, verbose_name='来店日時')),
                ('customer', models.ForeignKey(on_delete=True, to='core.Customer')),
            ],
            options={
                'db_table': 'customer_log',
                'ordering': ('-created_at',),
            },
        ),
    ]
