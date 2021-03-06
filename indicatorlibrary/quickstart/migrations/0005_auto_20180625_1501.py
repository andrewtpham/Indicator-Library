# Generated by Django 2.0.2 on 2018-06-25 15:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0004_auto_20180625_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additionalfields',
            name='additional_fields_uuid',
            field=models.CharField(blank=True, default=uuid.uuid4, max_length=500, unique=True, verbose_name='Additional Field UUID'),
        ),
        migrations.AlterField(
            model_name='frequency',
            name='frequency',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='frequency',
            name='frequency_uuid',
            field=models.CharField(blank=True, default=uuid.uuid4, max_length=500, unique=True, verbose_name='Frequency UUID'),
        ),
        migrations.AlterField(
            model_name='indicator',
            name='baseline',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='indicator',
            name='comments',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='indicator',
            name='data_collection_method',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Data Collection Method'),
        ),
        migrations.AlterField(
            model_name='indicator',
            name='denominator',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='indicator',
            name='disaggregation',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='indicator',
            name='indicator_uuid',
            field=models.TextField(blank=True, default=uuid.uuid4, max_length=500, unique=True, verbose_name='Indicator UUID'),
        ),
        migrations.AlterField(
            model_name='indicator',
            name='information_use',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Information Use'),
        ),
        migrations.AlterField(
            model_name='indicator',
            name='means_of_verification',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Means of Verification'),
        ),
        migrations.AlterField(
            model_name='indicator',
            name='method_of_analysis',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Method of Analysis'),
        ),
        migrations.AlterField(
            model_name='indicator',
            name='number',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='indicator',
            name='numerator',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='indicator',
            name='objectives',
            field=models.CharField(blank=True, max_length=500, verbose_name='Objective'),
        ),
        migrations.AlterField(
            model_name='indicator',
            name='rationale_for_target',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='indicator',
            name='responsible_person',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Responsible Person(s) and Team'),
        ),
        migrations.AlterField(
            model_name='indicator',
            name='sector',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='indicator',
            name='subsector',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='indicator',
            name='tags',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='indicator',
            name='unit_of_measure',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Unit of Measure'),
        ),
        migrations.AlterField(
            model_name='source',
            name='name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='source',
            name='source_uuid',
            field=models.CharField(blank=True, default=uuid.uuid4, max_length=500, unique=True, verbose_name='Source UUID'),
        ),
    ]
