# Generated by Django 4.0.5 on 2022-09-28 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_empgroup2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Months',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='statistics_Accounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Accounts_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='statistics_Accounts_Total',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Total', models.IntegerField(blank=True, default=0, null=True)),
                ('Accounts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.statistics_accounts')),
            ],
        ),
        migrations.CreateModel(
            name='statistics_Total_Voucher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Total', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='statistics_Voucher_count',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Total_Voucher', models.IntegerField(blank=True, default='', null=True)),
                ('Month', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.months')),
            ],
        ),
        migrations.CreateModel(
            name='statistics_Voucher_Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Particulars', models.CharField(max_length=255)),
                ('Debit_Amount', models.IntegerField(blank=True, default='', null=True)),
                ('Credit_Amount', models.IntegerField(blank=True, default='', null=True)),
                ('Month', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.months')),
            ],
        ),
        migrations.CreateModel(
            name='statistics_Vouchers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Vouchers_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='crtcompony',
        ),
        migrations.DeleteModel(
            name='empgroup',
        ),
        migrations.DeleteModel(
            name='empgroup2',
        ),
        migrations.AddField(
            model_name='statistics_voucher_register',
            name='Voucher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.statistics_vouchers'),
        ),
        migrations.AddField(
            model_name='statistics_voucher_count',
            name='Voucher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.statistics_vouchers'),
        ),
        migrations.AddField(
            model_name='statistics_total_voucher',
            name='Voucher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.statistics_vouchers'),
        ),
    ]