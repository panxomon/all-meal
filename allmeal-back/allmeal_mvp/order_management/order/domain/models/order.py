from django.db import models
from menu.domain.models.menu import Menu  # Asegúrate de importar correctamente el modelo Menu

class Order(models.Model):
    employee_id = models.CharField(max_length=100)  # Slack ID, nickname, etc.
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    def __str__(self):
        return f"Pedido de {self.employee_id} para {self.menu.name}"
