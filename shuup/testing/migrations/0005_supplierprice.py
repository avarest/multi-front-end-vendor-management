# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import shuup.utils.properties
import shuup.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shuup', '0051_supplier_enabled'),
        ('shuup_testing', '0004_fieldsmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupplierPrice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('amount_value', shuup.core.fields.MoneyValueField(max_digits=36, decimal_places=9)),
                ('product', models.ForeignKey(to='shuup.Product')),
                ('shop', models.ForeignKey(to='shuup.Shop')),
                ('supplier', models.ForeignKey(to='shuup.Supplier')),
            ],
            bases=(shuup.utils.properties.MoneyPropped, models.Model),
        ),
    ]
