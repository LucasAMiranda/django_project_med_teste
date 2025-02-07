from rest_framework import serializers
from .models import ProfissionalSaude, Consulta
from django.utils.html import strip_tags


class ProfissionalSaudeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfissionalSaude
        fields = '__all__'

    def validate_nome_completo(self, value):
        """Sanitiza e valida o nome completo"""
        value = strip_tags(value).strip()
        
        if len(value) < 5:
            raise serializers.ValidationError("O nome completo deve ter pelo menos 5 caracteres.")
        
        if " " not in value:
            raise serializers.ValidationError("Informe o nome completo com nome e sobrenome.")
        
        return value


    def validate_contato(self, value):
        """Valida se o contato segue um padrão de telefone"""
        import re
        pattern = r"^\(\d{2}\) \d{4,5}-\d{4}$"
        if not re.match(pattern, value):
            raise serializers.ValidationError("Formato de telefone inválido. Use: (XX) XXXXX-XXXX")
        return value



class ConsultaSerializer(serializers.ModelSerializer):
    profissional = ProfissionalSaudeSerializer(read_only=True)
    profissional_id = serializers.PrimaryKeyRelatedField(
        queryset=ProfissionalSaude.objects.all(), source="profissional", write_only=True
    )

    class Meta:
        model = Consulta
        fields = ['id', 'data_consulta', 'profissional', 'profissional_id']