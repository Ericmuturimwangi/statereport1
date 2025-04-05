from core.models import PDFSubmission, BrigadeReport, Unit, Brigade
from rest_framework import serializers

class PDFSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDFSubmission
        fields = '__all__'

class BrigadeReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrigadeReport
        fields = '__all__'

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'

class BrigadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brigade
        fields = '__all__'

