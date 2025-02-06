from rest_framework import serializers
from .models import ProfissionalSaude, Consulta

class ProfissionalSaudeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfissionalSaude
        fields = '__all__'


class ConsultaSerializer(serializers.ModelSerializer):
    profissional = ProfissionalSaudeSerializer(read_only=True)
    profissional_id = serializers.PrimaryKeyRelatedField(
        queryset=ProfissionalSaude.objects.all(), source="profissional", write_only=True
    )

    class Meta:
        model = Consulta
        fields = ['id', 'data_consulta', 'profissional', 'profissional_id']