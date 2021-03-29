# Generated by Django 3.1.7 on 2021-03-29 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': 'Компания', 'verbose_name_plural': 'Компании'},
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'Событие', 'verbose_name_plural': 'События'},
        ),
        migrations.AlterModelOptions(
            name='eventtime',
            options={'verbose_name': 'Время', 'verbose_name_plural': 'Время'},
        ),
        migrations.AlterModelOptions(
            name='russiacompany',
            options={'verbose_name': 'Русская компания', 'verbose_name_plural': 'Русские компании'},
        ),
        migrations.AddField(
            model_name='companytime',
            name='event',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='events.event'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Названия компании'),
        ),
        migrations.AlterField(
            model_name='event',
            name='date_events',
            field=models.DateField(verbose_name='Дата события'),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название события'),
        ),
        migrations.AlterField(
            model_name='russiacompany',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='russiacompany',
            name='fullname_representative',
            field=models.CharField(max_length=255, verbose_name='Полное имя представителя'),
        ),
        migrations.AlterField(
            model_name='russiacompany',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название компании'),
        ),
        migrations.AlterField(
            model_name='russiacompany',
            name='phone',
            field=models.CharField(max_length=50, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='russiacompany',
            name='position_representative',
            field=models.CharField(max_length=255, verbose_name='Долженость представителя'),
        ),
        migrations.AlterField(
            model_name='russiacompany',
            name='site',
            field=models.CharField(max_length=100, verbose_name='Сайт'),
        ),
    ]