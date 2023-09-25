# Generated by Django 4.2.5 on 2023-09-25 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
        migrations.AddField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='user_images'),
        ),
        migrations.AlterUniqueTogether(
            name='customuser',
            unique_together={('email',)},
        ),
    ]