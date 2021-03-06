# Generated by Django 3.0.8 on 2022-03-31 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0002_rename_profissão_cliente_profissao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='curriculo_upload',
            field=models.FileField(blank=True, null=True, upload_to='curriculos/%d/%m/%Y/'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(max_length=35),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
