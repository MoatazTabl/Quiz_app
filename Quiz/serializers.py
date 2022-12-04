from Quiz.models import QuesModel
from rest_framework import serializers


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuesModel
        fields = '__all__'
