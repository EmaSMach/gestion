from django.db import models
from django.utils.translation import gettext as _
# Create your models here.


class Province(models.Model):
    name = models.CharField(_("Nombre"), max_length=50)

    class Meta:
        verbose_name = 'Provincia'
        verbose_name_plural = 'Provincias'

    def __str__(self) -> str:
        return self.name


class City(models.Model):
    name = models.CharField(_("Ciudad"), max_length=50)
    province = models.ForeignKey(Province, verbose_name=_(
        "Provincia"), on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'

    def __str__(self) -> str:
        return self.name


class Address(models.Model):
    neighborhood = models.CharField(
        _("Barrio"), max_length=50, null=True, blank=True)
    street = models.CharField(_("Calle"), max_length=50, null=True, blank=True)
    number = models.CharField(
        _("Número"), max_length=50, null=True, blank=True)
    manzana = models.SmallIntegerField(_("Manzana"), null=True, blank=True)
    parcela = models.SmallIntegerField(_("Parcela"), null=True, blank=True)
    extra = models.TextField(_("Extra"), null=True, blank=True)
    city = models.ForeignKey(
        City, on_delete=models.PROTECT, related_name='addresses')

    class Meta:
        verbose_name = 'Domicilio'
        verbose_name_plural = 'Domicilios'

    def __str__(self) -> str:
        return f"{self.street} + {self.number} + {self.city}"


class Client(models.Model):
    code = models.CharField(_("Code"), max_length=50, primary_key=True)
    first_name = models.CharField(_("Nombre"), max_length=50)
    last_name = models.CharField(_("Apellido"), max_length=50)
    dni = models.IntegerField(_("DNI"), null=True, blank=True)
    address = models.ForeignKey(Address, verbose_name=_("Domicilio"), on_delete=models.PROTECT, null=True, blank=True,
                                related_name='clients')

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self) -> str:
        return f"({self.code}){self.first_name} {self.last_name}"
