# Generated by Django 3.1.7 on 2021-03-10 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210310_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinfo',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='budget',
            field=models.CharField(blank=True, choices=[('1000', '1000'), ('2000', '2000'), ('3000', '3000')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='company',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='contact',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='interested',
            field=models.CharField(blank=True, choices=[('school', 'school'), ('football', 'football'), ('music', 'music')], max_length=100, null=True),
        ),
    ]
