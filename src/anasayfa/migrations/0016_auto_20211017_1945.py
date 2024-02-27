# Generated by Django 3.2.4 on 2021-10-17 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anasayfa', '0015_clientopinionmodel_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioCatModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=40, verbose_name='İsim')),
                ('slug', models.SlugField(blank=True, max_length=500, null=True, verbose_name='uzantı')),
            ],
            options={
                'verbose_name': 'portfolyo kategöri',
                'verbose_name_plural': 'portfolyo kategöriler',
                'ordering': ['id'],
            },
        ),
        migrations.AlterField(
            model_name='clientsmodel',
            name='image',
            field=models.ImageField(null=True, upload_to='', verbose_name='ana resim "225x110"'),
        ),
        migrations.CreateModel(
            name='PortfolioModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=40, verbose_name='İsim')),
                ('small', models.CharField(blank=True, max_length=40, verbose_name='light text')),
                ('image', models.ImageField(null=True, upload_to='', verbose_name='ana resim ')),
                ('portfolyo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='portfoliocatmodelinline', to='anasayfa.portfoliocatmodel')),
            ],
            options={
                'verbose_name': 'portfolyo',
                'verbose_name_plural': 'portfolyolar',
                'ordering': ['id'],
            },
        ),
    ]