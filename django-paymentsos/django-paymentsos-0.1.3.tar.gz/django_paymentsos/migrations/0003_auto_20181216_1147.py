# Generated by Django 2.0.8 on 2018-12-16 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_paymentsos', '0002_paymentsosnotification_sub_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentsosnotification',
            name='result_status',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='paymentsosnotification',
            name='statement_soft_descriptor',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
