from django.db import models

# Create your models here.


class Grupos(models.Model):
    """
    Modelo que representa un grupo (p. ej. Todo en ventas, Ventas habana, etc.).
    """
    name = models.CharField(max_length=200, help_text="Ingrese el nombre del grupo (p. ej. Ventas Habana, etc.)")
    provincia = models.CharField(max_length=200, help_text="Ingrese el nombre de la provincia (p. ej. Pinar del Rio, La Habana, etc.)")
    municipio = models.CharField(max_length=200, help_text="Ingrese el nombre del municipio (p. ej. Vinales, etc.)")

    def __str__(self):
        """
        Cadena que representa a la instancia particular del modelo (p. ej. en el sitio de Administración)
        """
        return self.name,self.provincia,self.municipio



from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class Grupo(models.Model):
    """
    Modelo que representa un grupo (pero no un grupo específico).
    """

    title = models.CharField(max_length=200)

    #administrador = models.ForeignKey('Administrador', on_delete=models.SET_NULL, null=True)
    # ForeignKey, ya que un grupo tiene un solo administrador, pero el mismo administrador pudo haber creado muchos grupos.
    # 'administrador' es un string, en vez de un objeto, porque la clase administrador aún no ha sido declarada.

    resumen = models.TextField(max_length=1000, help_text="Ingrese una breve descripción del grupo")

    link = models.CharField('LINK',max_length=13, help_text='13 Caracteres <a href=""</a>')

    grupos = models.ManyToManyField(Grupos, help_text="Seleccione una provincia para este grupo ")
    # ManyToManyField, porque una provincia  puede contener muchos grupos y un grupo puede cubrir varios municipios.
    # La clase Grupos ya ha sido definida, entonces podemos especificar el objeto arriba.

    def __str__(self):
        """
        String que representa al objeto Grupo
        """
        return self.title


    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de Grupo
        """
        return reverse('grupo-detail', args=[str(self.id)])
