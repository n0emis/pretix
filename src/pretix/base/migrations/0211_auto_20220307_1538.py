# Generated by Django 3.2.12 on 2022-03-07 15:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0210_auto_20220304_0917'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartposition',
            name='discount',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='pretixbase.discount'),
        ),
        migrations.AddField(
            model_name='discount',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='orderposition',
            name='discount',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='pretixbase.discount'),
        ),
    ]
