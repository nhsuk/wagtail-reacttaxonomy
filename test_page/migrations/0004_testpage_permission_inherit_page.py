# Generated by Django 3.1.1 on 2020-09-04 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_page', '0003_auto_20200811_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='testpage',
            name='permission_inherit_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='test_page.testpage'),
        ),
    ]
