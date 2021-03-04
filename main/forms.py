from django.forms import ModelForm
from .models import Marks

class MarksForm(ModelForm):
    class Meta:
        model = Marks
        fields = ("roll_no", "name", "math_marks", "physics_marks","chemistry_marks")