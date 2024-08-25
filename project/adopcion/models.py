from django.contrib.auth.models import User
from django.db import models
from django.forms import ValidationError
from django.utils import timezone

class Adopcion(models.Model):
    adoptante = models.ForeignKey(User, on_delete=models.CASCADE)
    mascota = models.ForeignKey("mascota.Mascota", on_delete=models.CASCADE)
    fecha_adopcion = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        ordering = ("-fecha_adopcion",)

    def clean(self):
        if self.mascota.adoptada:
            raise ValidationError("Esta mascota ya fue adoptada")

    def save(self, *args, **kwargs):
        self.mascota.adoptada = True
        super().save(*args, **kwargs)