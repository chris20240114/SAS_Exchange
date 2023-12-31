# Generated by Django 4.1.1 on 2023-07-27 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seller',
            old_name='name',
            new_name='First_Name',
        ),
        migrations.AddField(
            model_name='seller',
            name='Last_Name',
            field=models.CharField(default=False, max_length=255),
        ),
        migrations.AlterField(
            model_name='seller',
            name='Experience',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=255),
        ),
        migrations.AlterField(
            model_name='seller',
            name='GroupChat',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=255),
        ),
    ]
