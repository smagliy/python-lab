from django.db import models


class TableHello(models.Model):
    name = models.CharField("Ім'я", max_length=50)
    surname = models.CharField("Прізвище", max_length=50)

    def __str__(self):
        return self.name

    class Meta:
         verbose_name = 'Таблиця коритувача'
         verbose_name_plural = 'Таблиця коритувачів'
         constraints = [
             models.UniqueConstraint(
                 fields=['name', 'surname'], name="unique_product_option"
             )
         ]