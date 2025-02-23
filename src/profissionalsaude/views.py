from django.shortcuts import render
from rest_framework import viewsets
from .models import ProfissionalSaude, Consulta
from .serializers import ProfissionalSaudeSerializer, ConsultaSerializer

# Create your views here.

class ProfissionalSaudeViewSet(viewsets.ModelViewSet):
    queryset = ProfissionalSaude.objects.all()
    serializer_class = ProfissionalSaudeSerializer

class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer