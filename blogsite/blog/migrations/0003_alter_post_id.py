# Generated by Django 4.1.1 on 2022-10-04 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.CharField(max_length=8, primary_key=True, serialize=False, verbose_name='v2KPdjg2'),
        ),
    ]
