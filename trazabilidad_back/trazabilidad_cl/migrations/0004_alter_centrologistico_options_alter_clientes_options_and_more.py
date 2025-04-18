# Generated by Django 5.1.6 on 2025-03-15 19:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trazabilidad_cl', '0003_centrologistico_grupoclientes_clientes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='centrologistico',
            options={'ordering': ['nombrecl']},
        ),
        migrations.AlterModelOptions(
            name='clientes',
            options={'ordering': ['cliente']},
        ),
        migrations.AlterModelOptions(
            name='grupoclientes',
            options={'ordering': ['grupocliente']},
        ),
        migrations.AlterModelOptions(
            name='tiposervicio',
            options={'ordering': ['nombre']},
        ),
        migrations.AlterField(
            model_name='clientes',
            name='nitcliente',
            field=models.BigIntegerField(unique=True, verbose_name='NIT Cliente'),
        ),
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ubicacion', models.CharField(max_length=50, verbose_name='Ubicación')),
                ('grupo', models.ForeignKey(limit_choices_to=models.Q(('tipo', models.F('tipo'))), on_delete=django.db.models.deletion.CASCADE, to='trazabilidad_cl.gruposervicio', verbose_name='Grupo de Servicio')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trazabilidad_cl.tiposervicio', verbose_name='Tipo de Servicio')),
            ],
        ),
    ]
