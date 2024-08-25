# Generated by Django 5.0.6 on 2024-05-18 19:21

from django.db import migrations

def sembrar(app, schema_editor):
  #usar esto en lugar del import de arriba
  Mascota = app.get_model("mascota","Mascota")

  for i in range(1, 10):
    Mascota.objects.create(
       nombre  = "Gato" + str(i),
       especie = "gato",
       tamano  ="mediano",
       edad    = str(i),
       descripcion = "Gato cargado automáticamente")   

class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0002_mascotacategoria_alter_mascota_options_and_more'),
    ]

    operations = [
       migrations.RunPython(sembrar)
    ]