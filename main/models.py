from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Marks(models.Model):
    roll_no = models.PositiveIntegerField(default = 1, validators = [MinValueValidator(1), MaxValueValidator(100)])
    name = models.CharField(max_length = 150)
    math_marks = models.PositiveIntegerField(default = 0, validators = [MinValueValidator(1), MaxValueValidator(100)])
    physics_marks = models.PositiveIntegerField(default = 0, validators = [MinValueValidator(1), MaxValueValidator(100)])
    chemistry_marks = models.PositiveIntegerField(default = 0, validators = [MinValueValidator(1), MaxValueValidator(100)])
    total = models.IntegerField(default = 0)
    percentage = models.DecimalField(max_digits = 5, decimal_places = 2)
    
    class Meta:
        verbose_name_plural = "Marks"
    
    def __str__(self):
        return str(self.roll_no) + " " + self.name