# Generated by Django 2.2.3 on 2019-07-05 03:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_one', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_two', models.CharField(blank=True, max_length=255, null=True)),
                ('company_name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_uploaded', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_eta', models.DateTimeField(blank=True, null=True)),
                ('quote_number', models.CharField(max_length=15)),
                ('reference', models.CharField(max_length=1000)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Client')),
                ('manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='QuoteItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=1000)),
                ('quantity', models.IntegerField(default=1)),
                ('part_number', models.CharField(blank=True, max_length=50, null=True)),
                ('quote_item_status', models.CharField(choices=[('APRSNG', 'Awaiting Processing'), ('PROCESSED', 'Processed'), ('AWAARIVAL', 'Awaiting Arrival'), ('ARRIVED', 'Arrived'), ('PENDING_FINANCE', 'Pending Approval'), ('NOTPAID_DELIVER', 'Not Paid, Allow Delivery'), ('PAID_DELIVER', 'Paid, Allow Delivery'), ('AWAITDELIVERY', 'Awaiting Delivery'), ('DELIVERED', 'Delivered'), ('NOTDELIVERED', 'Not Delivered')], max_length=20)),
                ('date_delivered', models.DateTimeField(blank=True, null=True)),
                ('date_processed', models.DateTimeField(blank=True, null=True)),
                ('date_arrived', models.DateTimeField(blank=True, null=True)),
                ('date_finance_approved', models.DateTimeField(blank=True, null=True)),
                ('quote', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Quote')),
            ],
        ),
    ]