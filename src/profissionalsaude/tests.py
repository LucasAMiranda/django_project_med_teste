from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import ProfissionalSaude


class ProfissionalSaudeAPITestCase(APITestCase):
    
    def setUp(self):
        """Configuração inicial antes dos testes"""
        self.user = User.objects.create_superuser(
            username="admin", password="admin123"
        )
        self.client.login(username="admin", password="admin123")

        self.profissional_data = {
            "nome_completo": "Dr. João Silva",
            "profissao": "Cardiologista",
            "endereco": "Rua das Flores, 123",
            "contato": "(11) 99999-9999",
            "nome_social": "Dr. João"
        }

    def test_criar_profissional_saude(self):
        """Testa a criação de um profissional de saúde via API"""
        response = self.client.post("/api/profissionais/", self.profissional_data, format="json")
        
        # Verifica se a resposta é 201 (Criado)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # Verifica se o profissional foi salvo corretamente
        self.assertEqual(ProfissionalSaude.objects.count(), 1)
        self.assertEqual(ProfissionalSaude.objects.first().nome_completo, "Dr. João Silva")
