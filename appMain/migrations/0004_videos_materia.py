# Generated by Django 4.1 on 2022-09-02 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appMain', '0003_materia'),
    ]

    operations = [
        migrations.AddField(
            model_name='videos',
            name='materia',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='appMain.materia'),
            preserve_default=False,
        ),
    ]