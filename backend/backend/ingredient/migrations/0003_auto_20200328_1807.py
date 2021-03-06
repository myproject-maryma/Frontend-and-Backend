# Generated by Django 2.2.7 on 2020-03-28 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ingredient', '0002_auto_20200328_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='ingredient.Category'),
        ),
    ]
