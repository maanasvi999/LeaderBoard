from rest_framework import serializers
from .models import Marks

class MarksSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name = "main:marks-detail")
    class Meta:
        model = Marks
        fields = ("url", "roll_no", "name", "total", "percentage", "math_marks", "physics_marks","chemistry_marks")