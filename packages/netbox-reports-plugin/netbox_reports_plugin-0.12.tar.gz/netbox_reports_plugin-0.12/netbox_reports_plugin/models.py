from django.db import models
from utilities.querysets import RestrictedQuerySet


class EquipmentData(models.Model):
    region = models.ForeignKey(
        to='dcim.Region',
        related_name='region_set_reports',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    city = models.ForeignKey(
        to='dcim.Region',
        related_name='city_set_reports',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    site = models.ForeignKey(
        to='dcim.Site',
        related_name='site_set_reports',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    device = models.ForeignKey(
        to='dcim.Device',
        related_name='devices_set_reports',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    manufacturer = models.ForeignKey(
        to='dcim.Manufacturer',
        related_name='manufacturer_set_reports',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    model = models.ForeignKey(
        to='dcim.DeviceType',
        related_name='model_set_reports',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    ip = models.ForeignKey(
        to='ipam.IPAddress',
        related_name='ip_set_reports',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    serial = models.CharField(
        max_length=400,
        blank=True,
        null=True
    )

    model_fact = models.CharField(
        max_length=400,
        blank=True,
        null=True
    )

    serial_fact = models.CharField(
        max_length=400,
        blank=True,
        null=True
    )

    date_create = models.DateTimeField(auto_now_add=True)

    error = models.TextField(
        max_length=500,
        blank=True,
        null=True
    )

    objects = RestrictedQuerySet.as_manager()

    def __str__(self):
        return f'{self.device}'

    class Meta:
        verbose_name_plural = 'Инвентаризация'
