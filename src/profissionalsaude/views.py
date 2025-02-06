from django.shortcuts import render
from rest_framework import viewsets
from .models import ProfissionalSaude
from .serializers import ProfissionalSaudeSerializer

# Create your views here.

class ProfissionalSaudeViewSet(viewsets.ModelViewSet):
    queryset = ProfissionalSaude.objects.all()
    serializer_class = ProfissionalSaudeSerializer

