import uuid
from django.db import models

class Menu(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField(null=True, blank=True)
    starter = models.CharField(max_length=100)  # Plato de entrada
    main_course = models.CharField(max_length=100)  # Plato principal
    dessert = models.CharField(max_length=100)  # Postre    

    def __str__(self):
        return f"Menu del {self.date}: {self.starter}, {self.main_course}, {self.dessert}"
    
    def to_dict(self):
        return {
            "id": self.id,
            "date": self.date,
            "starter": self.starter,
            "main_course": self.main_course,
            "dessert": self.dessert
        }
