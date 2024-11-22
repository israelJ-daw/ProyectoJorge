# Generated by Django 5.1.2 on 2024-10-31 10:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('premiun', models.BooleanField()),
                ('principal', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.FloatField(help_text='Total del pago')),
                ('fecha_pago', models.DateTimeField(auto_now_add=True)),
                ('metodo_pago', models.CharField(max_length=50)),
                ('cod_transaccion', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genero', models.CharField(max_length=10)),
                ('edad', models.PositiveIntegerField()),
                ('ubicacion', models.TextField()),
                ('biografia', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ServicioExtra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('precio', models.IntegerField()),
                ('disponible', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True)),
                ('telefono', models.CharField(blank=True, max_length=20)),
                ('fecha_registro', models.DateTimeField(db_column='fecha')),
            ],
        ),
        migrations.CreateModel(
            name='CategoriaPrincipal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('fecha_asignacion', models.DateTimeField()),
                ('prioridad', models.IntegerField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoria_principal', to='alquiler.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Propiedad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(editable=False, max_length=200)),
                ('direccion', models.CharField(max_length=200)),
                ('precio_por_noche', models.IntegerField()),
                ('max_usuarios', models.PositiveIntegerField()),
                ('categoria', models.ManyToManyField(related_name='propiedades', through='alquiler.CategoriaPrincipal', to='alquiler.categoria')),
                ('servicios_extra', models.ManyToManyField(related_name='propiedades', to='alquiler.servicioextra')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='propiedades', to='alquiler.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Prioridad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField(null=True)),
                ('premiun', models.BooleanField()),
                ('numero', models.IntegerField()),
                ('propiedades', models.ManyToManyField(related_name='prioridades', to='alquiler.propiedad')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField()),
                ('fecha_comentario', models.TimeField()),
                ('valoracion', models.IntegerField()),
                ('anonimo', models.BooleanField()),
                ('propiedad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='alquiler.propiedad')),
            ],
        ),
        migrations.AddField(
            model_name='categoriaprincipal',
            name='propiedad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoria_principal', to='alquiler.propiedad'),
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateTimeField()),
                ('total', models.FloatField()),
                ('estado', models.CharField(max_length=20)),
                ('pago', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reserva_pago', to='alquiler.pago')),
                ('perfil', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='reserva', to='alquiler.perfil')),
                ('propiedad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservas', to='alquiler.propiedad')),
            ],
        ),
        migrations.AddField(
            model_name='perfil',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='perfil', to='alquiler.usuario'),
        ),
    ]
